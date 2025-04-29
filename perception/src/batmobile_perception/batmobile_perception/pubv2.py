import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Point
from batmobile_perception import locate_func
from threading import Thread
import socket
import time
import json

# Global socket variable
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '192.168.0.24'
port = 8001


def connect_socket():
    """Ensure socket is connected to the server."""
    global client_socket
    while True:
        try:
            client_socket.connect((host, port))
            print(f"Connected to {host}:{port}")
            break
        except socket.error as e:
            print(f"Socket error: {e}, Retrying in 5 seconds...")
            time.sleep(5)  # Retry every 5 seconds


def socket_thread():
    """Thread to handle socket communication in background."""
    while rclpy.ok():
        try:
            # Perform socket communication if needed, or handle errors
            time.sleep(1)
        except socket.error as e:
            print(f"Socket error: {e}")
            print("Attempting to reconnect...")
            connect_socket()


class JokerFinder(Node):
    def __init__(self):
        super().__init__('target_location')
        self.pub = self.create_publisher(Point, 'get_point', 10)

        # Try to connect initially
        connect_socket()

        # Set up a timer for the callback
        timer_period = 1 / 24  # 24 Hz
        self.timer = self.create_timer(timer_period, self.callback)

        # Start socket communication thread
        self.socket_thread = Thread(target=socket_thread, daemon=True)
        self.socket_thread.start()

    def callback(self):
        msg = Point()
        status, x, y, z = locate_func.get_location()

        if not status:
            msg.x = 0.0
            msg.y = 0.0
            msg.z = 0.0
            self.get_logger().error("Sensor Data Unavailable")
        else:
            msg.x = x
            msg.y = y
            msg.z = z
            if (x, y, z) == (0.0, 0.0, 0.0):
                self.get_logger().info("Object not detected")
            else:
                self.get_logger().info(f"Object detected at {x}, {y}, {z}")

        # Prepare data to send over socket as JSON
        data = json.dumps({"x": msg.x, "y": msg.y, "z": msg.z})
        
        # Attempt to send data over the socket
        try:
            client_socket.send(data.encode())
        except socket.error as e:
            self.get_logger().error(f"Socket error: {e}")
            self.get_logger().info("Reconnecting to socket...")
            connect_socket()  # Reconnect to the socket if it was closed

        # Publish the message
        self.pub.publish(msg)


def main(args=None):
    rclpy.init(args=args)

    # Create and start the publisher node
    publisher = JokerFinder()

    rclpy.spin(publisher)

    # Close the socket when done
    client_socket.close()


if __name__ == '__main__':
    main()
