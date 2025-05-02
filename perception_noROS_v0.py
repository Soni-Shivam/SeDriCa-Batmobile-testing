import pyrealsense2 as rs
import socket
import struct
import time
import numpy as np
import cv2
from ultralytics import YOLO

# IP and port of Raspberry Pi server
host = '192.168.0.182'
port = 8001
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Image dimensions
img_w = 640
img_h = 480

# Load YOLO model
model = YOLO("/home/nvidia/freshies/SeDriCa-BatMobile-v2/src/batmobile_perception/best.pt")

# RealSense configuration
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
depth_intrinsics = profile.get_stream(rs.stream.depth).as_video_stream_profile().get_intrinsics()

# Function to connect to the server socket
def connect_socket():
    while True:
        try:
            client_socket.connect((host, port))
            print(f"[INFO] Connected to server at {host}:{port}")
            break
        except socket.error as e:
            print(f"[WARN] Connection failed: {e}, retrying in 2 seconds...")
            time.sleep(2)

# Function to get object location using YOLO and depth
def get_location():
    try:
        frames = pipeline.wait_for_frames()
        aligned_frames = align.process(frames)
        depth_frame = aligned_frames.get_depth_frame()
        color_frame = aligned_frames.get_color_frame()

        if not depth_frame or not color_frame:
            return (0, 0.0, 0.0, 0.0)

        depth_image = np.asanyarray(depth_frame.get_data())
        color_image = np.asanyarray(color_frame.get_data())
        rgb_image = cv2.cvtColor(color_image, cv2.COLOR_BGR2RGB)

        result = model(rgb_image, conf=0.2)

        for r in result:
            boxes = r.boxes.xywh.cpu().numpy()
            confidences = r.boxes.conf.cpu().numpy()
            class_ids = r.boxes.cls.cpu().numpy()

            for vector, conf, clid in zip(boxes, confidences, class_ids):
                xc, yc, w, h = vector
                xc, yc = int(xc), int(yc)

                if 0 <= xc < depth_image.shape[1] and 0 <= yc < depth_image.shape[0]:
                    depth_value = depth_frame.get_distance(xc, yc)
                    X, Y, Z = rs.rs2_deproject_pixel_to_point(color_intrinsics, [xc, yc], depth_value)
                    return (1, X, Y, Z)

        return (1, 0.0, 0.0, 0.0)

    except Exception as e:
        print(f"[ERROR] Exception in get_location: {e}")
        return (0, 0.0, 0.0, 0.0)

# Start socket connection
connect_socket()

# Main loop
try:
    while True:
        status, x, y, z = get_location()
        print(f"({x:.2f},{y:.2f},{z:.2f})")
        if not status:
            x, y, z = 0.0, 0.0, 0.0

        data_str = f"({x:.2f},{y:.2f},{z:.2f})"
        data_bytes = data_str.encode('utf-8')
        header = struct.pack('!I', len(data_bytes))

        try:
            client_socket.sendall(header + data_bytes)
        except socket.error as e:
            print(f"[ERROR] Send failed: {e}, reconnecting...")
            connect_socket()

except KeyboardInterrupt:
    print("[INFO] Loop interrupted by user")

finally:
    pipeline.stop()
    client_socket.close()
    print("[INFO] Resources released and program exited cleanly.")
