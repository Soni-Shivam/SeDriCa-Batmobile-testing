import pyrealsense2 as rs
import socket
import struct
import time
import numpy as np
import cv2
import tensorrt as trt
import pycuda.driver as cuda
import pycuda.autoinit  # Initializes CUDA driver

# Paths
ENGINE_PATH = "/home/nvidia/TensorRT/best.engine"

# Socket config
host = '192.168.0.182'
port = 8001
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Image dimensions
img_w, img_h = 640, 480

# RealSense setup
pipeline = rs.pipeline()
config = rs.config()
config.enable_stream(rs.stream.color, img_w, img_h, rs.format.bgr8, 30)
config.enable_stream(rs.stream.depth, img_w, img_h, rs.format.z16, 30)
align_to = rs.stream.color
align = rs.align(align_to)

pipeline.start(config)
profile = pipeline.get_active_profile()
color_intrinsics = profile.get_stream(rs.stream.color).as_video_stream_profile().get_intrinsics()

# TensorRT engine loading
TRT_LOGGER = trt.Logger(trt.Logger.INFO)
with open(ENGINE_PATH, "rb") as f, trt.Runtime(TRT_LOGGER) as runtime:
    engine = runtime.deserialize_cuda_engine(f.read())
context = engine.create_execution_context()

# Bindings setup
input_shape = (1, 3, img_h, img_w)
output_shape = (1, 25200, 85)  # Adjust this based on your YOLO model
input_binding_idx = engine.get_binding_index(engine.get_binding_name(0))
output_binding_idx = engine.get_binding_index(engine.get_binding_name(1))

# Allocate buffers
d_input = cuda.mem_alloc(np.prod(input_shape).astype(np.int32) * 4)
d_output = cuda.mem_alloc(np.prod(output_shape).astype(np.int32) * 4)
bindings = [int(d_input), int(d_output)]
stream = cuda.Stream()

# Socket connection
def connect_socket():
    while True:
        try:
            client_socket.connect((host, port))
            print(f"[INFO] Connected to server at {host}:{port}")
            break
        except socket.error as e:
            print(f"[WARN] Connection failed: {e}, retrying in 2 seconds...")
            time.sleep(2)

# Preprocess image
def preprocess(image):
    image = cv2.resize(image, (img_w, img_h))
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = np.transpose(image, (2, 0, 1)).astype(np.float32)
    image /= 255.0
    return np.expand_dims(image, axis=0)

# Postprocess (simplified, assumes 1 object max)
def postprocess(output, conf_thres=0.2):
    boxes = output[0]
    for b in boxes:
        if b[4] > conf_thres:
            scores = b[5:]
            cls_id = np.argmax(scores)
            xc, yc, w, h = b[:4]
            return int(xc * img_w), int(yc * img_h), cls_id, b[4]
    return None

# Main function to get object location
def get_location():
    try:
        frames = pipeline.wait_for_frames()
        aligned = align.process(frames)
        color_frame = aligned.get_color_frame()
        depth_frame = aligned.get_depth_frame()

        if not color_frame or not depth_frame:
            return (0, 0.0, 0.0, 0.0)

        color_image = np.asanyarray(color_frame.get_data())
        depth_image = np.asanyarray(depth_frame.get_data())

        input_image = preprocess(color_image)
        cuda.memcpy_htod_async(d_input, input_image, stream)
        context.execute_async_v2(bindings=bindings, stream_handle=stream.handle)
        output = np.empty(output_shape, dtype=np.float32)
        cuda.memcpy_dtoh_async(output, d_output, stream)
        stream.synchronize()

        detection = postprocess(output)
        if detection:
            xc, yc, cls_id, conf = detection
            depth_value = depth_frame.get_distance(xc, yc)
            X, Y, Z = rs.rs2_deproject_pixel_to_point(color_intrinsics, [xc, yc], depth_value)
            return (1, X, Y, Z)

        return (1, 0.0, 0.0, 0.0)

    except Exception as e:
        print(f"[ERROR] {e}")
        return (0, 0.0, 0.0, 0.0)

# Run
connect_socket()
try:
    while True:
        status, x, y, z = get_location()
        print(f"({x:.2f},{y:.2f},{z:.2f})")
        if not status:
            x, y, z = 0.0, 0.0, 0.0
        data = f"({x:.2f},{y:.2f},{z:.2f})".encode('utf-8')
        header = struct.pack('!I', len(data))
        try:
            client_socket.sendall(header + data)
        except socket.error as e:
            print(f"[ERROR] Send failed: {e}, reconnecting...")
            connect_socket()
except KeyboardInterrupt:
    print("[INFO] Interrupted")
finally:
    pipeline.stop()
    client_socket.close()
