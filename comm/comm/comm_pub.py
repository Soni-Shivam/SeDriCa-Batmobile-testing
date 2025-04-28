import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Point
import socket


class PublisherNode(Node):
    def __init__(self):
        super().__init__('get_point')
        self.publisher_ = self.create_publisher(Point, 'socket_messages', 10)
        self.host = '0.0.0.0'
        self.port = 8001
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(1)
        self.get_logger().info(f"Socket server listening on {self.host}:{self.port}")
        self.accept_and_receive()

    def accept_and_receive(self):
        while rclpy.ok():
            self.get_logger().info("Waiting for a connection...")
            client_socket, client_address = self.server_socket.accept()
            self.get_logger().info(f"Connection established with {client_address}")

            try:
                message = client_socket.recv(1024).decode()
                self.get_logger().info(f"Message received: {message}")
                msg = Point()
                msg.data = message
                self.publisher_.publish(msg)
                self.get_logger().info(f"Published message to topic 'socket_messages'")

            except Exception as e:
                self.get_logger().error(f"Error receiving message: {e}")
            finally:
                client_socket.close()
                self.get_logger().info(f"Connection with {client_address} closed.")

def main(args=None):
    rclpy.init(args=args)
    node = PublisherNode()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info("Keyboard interrupt, shutting down node.")
    finally:
        node.server_socket.close()
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
