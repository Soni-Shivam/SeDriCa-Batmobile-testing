import pyrealsense2 as rs
import time
import numpy as np
import cv2
import pycuda.driver as cuda
import pycuda.autoinit
import tensorrt as trt

# Image dimensions
img_w = 640
img_h = 480

# Load TensorRT engine
TRT_LOGGER = trt.Logger(trt.Logger.WARNING)

def load_engine(engine_file):
    with open(engine_file, "rb") as f:
        engine_data = f.read()
    runtime = trt.Runtime(TRT_LOGGER)
    return runtime.deserialize_cuda_engine(engine_data)

engine = load_engine("/home/nvidia/TensorRT/best.engine")
context = engine.create_execution_context()

# List engine bindings for reference
print("Engine has", engine.num_bindings, "bindings:")
for idx in range(engine.num_bindings):
    name = engine.get_binding_name(idx)
    is_input = engine.binding_is_input(idx)
    shape = engine.get_binding_shape(idx)
    print(f"  idx={idx:2d} | {'IN ' if is_input else 'OUT'} | name='{name}' | shape={shape}")

# Use actual binding names from the engine
INPUT_NAME = "images"       # replace with the printed input name
OUTPUT_NAME = "output0"     # replace with the desired output binding

# Get binding indices
input_index = engine.get_binding_index(INPUT_NAME)
output_index = engine.get_binding_index(OUTPUT_NAME)

# Get binding shapes
tensor_input_shape = tuple(engine.get_binding_shape(input_index))
tensor_output_shape = tuple(engine.get_binding_shape(output_index))

# Compute buffer sizes
input_size = np.prod(tensor_input_shape) * np.dtype(np.float32).itemsize
output_size = np.prod(tensor_output_shape) * np.dtype(np.float32).itemsize

d_input = cuda.mem_alloc(input_size)
d_output = cuda.mem_alloc(output_size)
bindings = [int(d_input), int(d_output)]

#camera setup
pipeline = rs.pipeline()
config = rs.config()
config.enable_stream(rs.stream.color, img_w, img_h, rs.format.bgr8, 30)
config.enable_stream(rs.stream.depth, img_w, img_h, rs.format.z16, 30)

align_to = rs.stream.color
align = rs.align(align_to)

pipeline.start(config)
profile = pipeline.get_active_profile()
depth_sensor = profile.get_device().first_depth_sensor()
depth_scale = depth_sensor.get_depth_scale()
color_intrinsics = profile.get_stream(rs.stream.color).as_video_stream_profile().get_intrinsics()

def get_location():
    frames = pipeline.wait_for_frames()
    aligned = align.process(frames)
    depth_frame = aligned.get_depth_frame()
    color_frame = aligned.get_color_frame()
    if not depth_frame or not color_frame:
        return None

    depth_image = np.asanyarray(depth_frame.get_data())
    color_image = np.asanyarray(color_frame.get_data())
    rgb = cv2.cvtColor(color_image, cv2.COLOR_BGR2RGB)

    # Prepare input for inference
    inp = np.ascontiguousarray(rgb).astype(np.float32) / 255.0
    cuda.memcpy_htod(d_input, inp.ravel())

    # Run inference
    context.execute_v2(bindings)

    # Retrieve output
    output = np.empty(tensor_output_shape, dtype=np.float32)
    cuda.memcpy_dtoh(output, d_output)

    # Flatten detections and parse (example for YOLO-like)
    detections = output.reshape(-1, tensor_output_shape[-1])
    for det in detections:
        xc, yc, w, h, conf = det[:5]
        if conf > 0.2:
            x_pix = int(xc * img_w)
            y_pix = int(yc * img_h)
            if 0 <= x_pix < img_w and 0 <= y_pix < img_h:
                dist = depth_frame.get_distance(x_pix, y_pix)
                X, Y, Z = rs.rs2_deproject_pixel_to_point(color_intrinsics, [x_pix, y_pix], dist)
                return X, Y, Z
    return None
# Perception loop
try:
    while True:
        loc = get_location()
        if loc:
            X, Y, Z = loc
            print(f"Detected at (X={X:.3f}, Y={Y:.3f}, Z={Z:.3f})")
        else:
            print("No detection")
        time.sleep(0.1)

except KeyboardInterrupt:
    pass

finally:
    pipeline.stop()
    print("Pipeline stopped. Exiting.")
                                                      
