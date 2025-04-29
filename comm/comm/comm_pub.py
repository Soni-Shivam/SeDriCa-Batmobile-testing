# import rclpy
# from rclpy.node import Node
# from geometry_msgs.msg import Point
# import socket


# class PublisherNode(Node):
#     def __init__(self):
#         super().__init__('get_point')
#         self.publisher_ = self.create_publisher(Point, 'socket_messages', 10)
#         self.host = '0.0.0.0'
#         self.port = 8001
#         self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         self.server_socket.bind((self.host, self.port))
#         self.server_socket.listen(1)
#         self.get_logger().info(f"Socket server listening on {self.host}:{self.port}")
#         self.accept_and_receive()

#     def accept_and_receive(self):
#         while rclpy.ok():
#             self.get_logger().info("Waiting for a connection...")
#             client_socket, client_address = self.server_socket.accept()
#             self.get_logger().info(f"Connection established with {client_address}")

#             try:
#                 message = client_socket.recv(1024).decode()
#                 self.get_logger().info(f"Message received: {message}")
#                 msg = Point()
#                 msg.data = message
#                 self.publisher_.publish(msg)
#                 self.get_logger().info(f"Published message to topic 'socket_messages'")

#             except Exception as e:
#                 self.get_logger().error(f"Error receiving message: {e}")
#             finally:
#                 client_socket.close()
#                 self.get_logger().info(f"Connection with {client_address} closed.")

# def main(args=None):
#     rclpy.init(args=args)
#     node = PublisherNode()

#     try:
#         rclpy.spin(node)
#     except KeyboardInterrupt:
#         node.get_logger().info("Keyboard interrupt, shutting down node.")
#     finally:
#         node.server_socket.close()
#         node.destroy_node()
#         rclpy.shutdown()

# if __name__ == '__main__':
#     main()



import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Point
import socket
import struct
from threading import Thread


def recv_all(sock, n):
    """
    Helper function to receive exactly n bytes from the socket.
    Raises EOFError if the connection is closed before n bytes are read.
    """
    data = b''
    while len(data) < n:
        chunk = sock.recv(n - len(data))
        if not chunk:
            # Connection closed prematurely
            raise EOFError('Socket closed before receiving all data')
        data += chunk
    return data


class SocketBridgeNode(Node):
    """
    A ROS2 node that bridges incoming socket messages to geometry_msgs/Point topics.
    Receives string messages of the form "(x, y, z)" and converts to Point.
    """
    def __init__(self):
        super().__init__('socket_bridge')
        # Publisher for geometry_msgs/Point messages on topic 'socket_messages'
        self.publisher_ = self.create_publisher(Point, 'socket_messages', 10)

        # Server configuration
        self.host = '0.0.0.0'  # Listen on all interfaces
        self.port = 8001       # Port number

        # Create, bind, and listen on the server socket
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(1)
        self.get_logger().info(f"Socket server listening on {self.host}:{self.port}")

        # Start accept loop in background so ROS callbacks can run
        accept_thread = Thread(target=self.accept_and_receive, daemon=True)
        accept_thread.start()

    def accept_and_receive(self):
        """
        Main loop for accepting new client connections and receiving messages.
        Uses length-prefixed framing to read complete string payloads.
        Expected message format: "(x, y, z)"
        """
        while rclpy.ok():
            self.get_logger().info('Waiting for a new client connection...')
            try:
                client_socket, client_address = self.server_socket.accept()
                self.get_logger().info(f'Accepted connection from {client_address}')

                # Handle messages from this client until disconnect
                while rclpy.ok():
                    # First read 4 bytes for the payload length
                    length_bytes = recv_all(client_socket, 4)
                    msg_length = struct.unpack('!I', length_bytes)[0]

                    # Then read the full payload
                    payload_bytes = recv_all(client_socket, msg_length)
                    message_str = payload_bytes.decode('utf-8')
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Point
import socket
import struct
from threading import Thread


def recv_all(sock, n):
    """
    Helper function to receive exactly n bytes from the socket.
    Raises EOFError if the connection is closed before n bytes are read.
    """
    data = b''
    while len(data) < n:
        chunk = sock.recv(n - len(data))
        if not chunk:
            # Connection closed prematurely
            raise EOFError('Socket closed before receiving all data')
        data += chunk
    return data


class SocketBridgeNode(Node):
    """
    A ROS2 node that bridges incoming socket messages to geometry_msgs/Point topics.
    Receives string messages of the form "(x, y, z)" and converts to Point.
    """
    def __init__(self):
        super().__init__('socket_bridge')
        # Publisher for geometry_msgs/Point messages on topic 'socket_messages'
        self.publisher_ = self.create_publisher(Point, 'socket_messages', 10)

        # Server configuration
        self.host = '0.0.0.0'  # Listen on all interfaces
        self.port = 8001       # Port number

        # Create, bind, and listen on the server socket
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(1)
        self.get_logger().info(f"Socket server listening on {self.host}:{self.port}")

        # Start accept loop in background so ROS callbacks can run
        accept_thread = Thread(target=self.accept_and_receive, daemon=True)
        accept_thread.start()

    def accept_and_receive(self):
        """
        Main loop for accepting new client connections and receiving messages.
        Uses length-prefixed framing to read complete string payloads.
        Expected message format: "(x, y, z)"
        """
        while rclpy.ok():
            self.get_logger().info('Waiting for a new client connection...')
            try:
                client_socket, client_address = self.server_socket.accept()
                self.get_logger().info(f'Accepted connection from {client_address}')

                # Handle messages from this client until disconnect
                while rclpy.ok():
                    # First read 4 bytes for the payload length
                    length_bytes = recv_all(client_socket, 4)
                    msg_length = struct.unpack('!I', length_bytes)[0]

                    # Then read the full payload
                    payload_bytes = recv_all(client_socket, msg_length)
                    message_str = payload_bytes.decode('utf-8')

                    # Parse the string into Point
                    try:
                        message_str = message_str.strip().strip('()')
                        x_str, y_str, z_str = message_str.split(',')
                        point = Point()
                        point.x = float(x_str)
                        point.y = float(y_str)
                        point.z = float(z_str)

                        # Publish to ROS2 topic
                        self.publisher_.publish(point)
                        self.get_logger().info(f"Published Point(x={point.x}, y={point.y}, z={point.z})")
                    except Exception as parse_error:
                        self.get_logger().error(f"Failed to parse message '{message_str}': {parse_error}")

            except EOFError:
                # Client disconnected cleanly
                self.get_logger().info(f'Client {client_address} disconnected')
            except Exception as e:
                # Log any other errors
                self.get_logger().error(f'Error in socket receive loop: {e}')
            finally:
                # Always close the client socket
                try:
                    client_socket.close()
                except Exception:
                    pass
                self.get_logger().info(f'Closed connection with {client_address}')

    def destroy(self):
        """
        Cleanup the server socket when shutting down.
        """
        self.get_logger().info('Shutting down socket server')
        self.server_socket.close()
        super().destroy_node()


def main(args=None):
    rclpy.init(args=args)
    node = SocketBridgeNode()

    try:
        # Keep the node alive to process ROS callbacks
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info('Keyboard interrupt received, shutting down')
    finally:
        # Clean up sockets and destroy the node
        node.destroy()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Point
import socket
import struct
from threading import Thread


def recv_all(sock, n):
    """
    Helper function to receive exactly n bytes from the socket.
    Raises EOFError if the connection is closed before n bytes are read.
    """
    data = b''
    while len(data) < n:
        chunk = sock.recv(n - len(data))
        if not chunk:
            # Connection closed prematurely
            raise EOFError('Socket closed before receiving all data')
        data += chunk
    return data


class SocketBridgeNode(Node):
    """
    A ROS2 node that bridges incoming socket messages to geometry_msgs/Point topics.
    Receives string messages of the form "(x, y, z)" and converts to Point.
    """
    def __init__(self):
        super().__init__('socket_bridge')
        # Publisher for geometry_msgs/Point messages on topic 'socket_messages'
        self.publisher_ = self.create_publisher(Point, 'socket_messages', 10)

        # Server configuration
        self.host = '0.0.0.0'  # Listen on all interfaces
        self.port = 8001       # Port number

        # Create, bind, and listen on the server socket
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(1)
        self.get_logger().info(f"Socket server listening on {self.host}:{self.port}")

        # Start accept loop in background so ROS callbacks can run
        accept_thread = Thread(target=self.accept_and_receive, daemon=True)
        accept_thread.start()

    def accept_and_receive(self):
        """
        Main loop for accepting new client connections and receiving messages.
        Uses length-prefixed framing to read complete string payloads.
        Expected message format: "(x, y, z)"
        """
        while rclpy.ok():
            self.get_logger().info('Waiting for a new client connection...')
            try:
                client_socket, client_address = self.server_socket.accept()
                self.get_logger().info(f'Accepted connection from {client_address}')

                # Handle messages from this client until disconnect
                while rclpy.ok():
                    # First read 4 bytes for the payload length
                    length_bytes = recv_all(client_socket, 4)
                    msg_length = struct.unpack('!I', length_bytes)[0]

                    # Then read the full payload
                    payload_bytes = recv_all(client_socket, msg_length)
                    message_str = payload_bytes.decode('utf-8')

                    # Parse the string into Point
                    try:
                        message_str = message_str.strip().strip('()')
                        x_str, y_str, z_str = message_str.split(',')
                        point = Point()
                        point.x = float(x_str)
                        point.y = float(y_str)
                        point.z = float(z_str)

                        # Publish to ROS2 topic
                        self.publisher_.publish(point)
                        self.get_logger().info(f"Published Point(x={point.x}, y={point.y}, z={point.z})")
                    except Exception as parse_error:
                        self.get_logger().error(f"Failed to parse message '{message_str}': {parse_error}")

            except EOFError:
                # Client disconnected cleanly
                self.get_logger().info(f'Client {client_address} disconnected')
            except Exception as e:
                # Log any other errors
                self.get_logger().error(f'Error in socket receive loop: {e}')
            finally:
                # Always close the client socket
                try:
                    client_socket.close()
                except Exception:
                    pass
                self.get_logger().info(f'Closed connection with {client_address}')

    def destroy(self):
        """
        Cleanup the server socket when shutting down.
        """
        self.get_logger().info('Shutting down socket server')
        self.server_socket.close()
        super().destroy_node()


def main(args=None):
    rclpy.init(args=args)
    node = SocketBridgeNode()

    try:
        # Keep the node alive to process ROS callbacks
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info('Keyboard interrupt received, shutting down')
    finally:
        # Clean up sockets and destroy the node
        node.destroy()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Point
import socket
import struct
from threading import Thread


def recv_all(sock, n):
    """
    Helper function to receive exactly n bytes from the socket.
    Raises EOFError if the connection is closed before n bytes are read.
    """
    data = b''
    while len(data) < n:
        chunk = sock.recv(n - len(data))
        if not chunk:
            # Connection closed prematurely
            raise EOFError('Socket closed before receiving all data')
        data += chunk
    return data


class SocketBridgeNode(Node):
    """
    A ROS2 node that bridges incoming socket messages to geometry_msgs/Point topics.
    Receives string messages of the form "(x, y, z)" and converts to Point.
    """
    def __init__(self):
        super().__init__('socket_bridge')
        # Publisher for geometry_msgs/Point messages on topic 'socket_messages'
        self.publisher_ = self.create_publisher(Point, 'socket_messages', 10)

        # Server configuration
        self.host = '0.0.0.0'  # Listen on all interfaces
        self.port = 8001       # Port number

        # Create, bind, and listen on the server socket
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(1)
        self.get_logger().info(f"Socket server listening on {self.host}:{self.port}")

        # Start accept loop in background so ROS callbacks can run
        accept_thread = Thread(target=self.accept_and_receive, daemon=True)
        accept_thread.start()

    def accept_and_receive(self):
        """
        Main loop for accepting new client connections and receiving messages.
        Uses length-prefixed framing to read complete string payloads.
        Expected message format: "(x, y, z)"
        """
        while rclpy.ok():
            self.get_logger().info('Waiting for a new client connection...')
            try:
                client_socket, client_address = self.server_socket.accept()
                self.get_logger().info(f'Accepted connection from {client_address}')

                # Handle messages from this client until disconnect
                while rclpy.ok():
                    # First read 4 bytes for the payload length
                    length_bytes = recv_all(client_socket, 4)
                    msg_length = struct.unpack('!I', length_bytes)[0]

                    # Then read the full payload
                    payload_bytes = recv_all(client_socket, msg_length)
                    message_str = payload_bytes.decode('utf-8')

                    # Parse the string into Point
                    try:
                        message_str = message_str.strip().strip('()')
                        x_str, y_str, z_str = message_str.split(',')
                        point = Point()
                        point.x = float(x_str)
                        point.y = float(y_str)
                        point.z = float(z_str)

                        # Publish to ROS2 topic
                        self.publisher_.publish(point)
                        self.get_logger().info(f"Published Point(x={point.x}, y={point.y}, z={point.z})")
                    except Exception as parse_error:
                        self.get_logger().error(f"Failed to parse message '{message_str}': {parse_error}")

            except EOFError:
                # Client disconnected cleanly
                self.get_logger().info(f'Client {client_address} disconnected')
            except Exception as e:
                # Log any other errors
                self.get_logger().error(f'Error in socket receive loop: {e}')
            finally:
                # Always close the client socket
                try:
                    client_socket.close()
                except Exception:
                    pass
                self.get_logger().info(f'Closed connection with {client_address}')

    def destroy(self):
        """
        Cleanup the server socket when shutting down.
        """
        self.get_logger().info('Shutting down socket server')
        self.server_socket.close()
        super().destroy_node()


def main(args=None):
    rclpy.init(args=args)
    node = SocketBridgeNode()

    try:
        # Keep the node alive to process ROS callbacks
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info('Keyboard interrupt received, shutting down')
    finally:
        # Clean up sockets and destroy the node
        node.destroy()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Point
import socket
import struct
from threading import Thread


def recv_all(sock, n):
    """
    Helper function to receive exactly n bytes from the socket.
    Raises EOFError if the connection is closed before n bytes are read.
    """
    data = b''
    while len(data) < n:
        chunk = sock.recv(n - len(data))
        if not chunk:
            # Connection closed prematurely
            raise EOFError('Socket closed before receiving all data')
        data += chunk
    return data


class SocketBridgeNode(Node):
    """
    A ROS2 node that bridges incoming socket messages to geometry_msgs/Point topics.
    Receives string messages of the form "(x, y, z)" and converts to Point.
    """
    def __init__(self):
        super().__init__('socket_bridge')
        # Publisher for geometry_msgs/Point messages on topic 'socket_messages'
        self.publisher_ = self.create_publisher(Point, 'socket_messages', 10)

        # Server configuration
        self.host = '0.0.0.0'  # Listen on all interfaces
        self.port = 8001       # Port number

        # Create, bind, and listen on the server socket
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(1)
        self.get_logger().info(f"Socket server listening on {self.host}:{self.port}")

        # Start accept loop in background so ROS callbacks can run
        accept_thread = Thread(target=self.accept_and_receive, daemon=True)
        accept_thread.start()

    def accept_and_receive(self):
        """
        Main loop for accepting new client connections and receiving messages.
        Uses length-prefixed framing to read complete string payloads.
        Expected message format: "(x, y, z)"
        """
        while rclpy.ok():
            self.get_logger().info('Waiting for a new client connection...')
            try:
                client_socket, client_address = self.server_socket.accept()
                self.get_logger().info(f'Accepted connection from {client_address}')

                # Handle messages from this client until disconnect
                while rclpy.ok():
                    # First read 4 bytes for the payload length
                    length_bytes = recv_all(client_socket, 4)
                    msg_length = struct.unpack('!I', length_bytes)[0]

                    # Then read the full payload
                    payload_bytes = recv_all(client_socket, msg_length)
                    message_str = payload_bytes.decode('utf-8')

                    # Parse the string into Point
                    try:
                        message_str = message_str.strip().strip('()')
                        x_str, y_str, z_str = message_str.split(',')
                        point = Point()
                        point.x = float(x_str)
                        point.y = float(y_str)
                        point.z = float(z_str)

                        # Publish to ROS2 topic
                        self.publisher_.publish(point)
                        self.get_logger().info(f"Published Point(x={point.x}, y={point.y}, z={point.z})")
                    except Exception as parse_error:
                        self.get_logger().error(f"Failed to parse message '{message_str}': {parse_error}")

            except EOFError:
                # Client disconnected cleanly
                self.get_logger().info(f'Client {client_address} disconnected')
            except Exception as e:
                # Log any other errors
                self.get_logger().error(f'Error in socket receive loop: {e}')
            finally:
                # Always close the client socket
                try:
                    client_socket.close()
                except Exception:
                    pass
                self.get_logger().info(f'Closed connection with {client_address}')

    def destroy(self):
        """
        Cleanup the server socket when shutting down.
        """
        self.get_logger().info('Shutting down socket server')
        self.server_socket.close()
        super().destroy_node()


def main(args=None):
    rclpy.init(args=args)
    node = SocketBridgeNode()

    try:
        # Keep the node alive to process ROS callbacks
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info('Keyboard interrupt received, shutting down')
    finally:
        # Clean up sockets and destroy the node
        node.destroy()
        rclpy.shutdown()


if __name__ == '__main__':
    main()

                    # Parse the string into Point
                    try:
                        message_str = message_str.strip().strip('()')
                        x_str, y_str, z_str = message_str.split(',')
                        point = Point()
                        point.x = float(x_str)
                        point.y = float(y_str)
                        point.z = float(z_str)

                        # Publish to ROS2 topic
                        self.publisher_.publish(point)
                        self.get_logger().info(f"Published Point(x={point.x}, y={point.y}, z={point.z})")
                    except Exception as parse_error:
                        self.get_logger().error(f"Failed to parse message '{message_str}': {parse_error}")

            except EOFError:
                # Client disconnected cleanly
                self.get_logger().info(f'Client {client_address} disconnected')
            except Exception as e:
                # Log any other errors
                self.get_logger().error(f'Error in socket receive loop: {e}')
            finally:
                # Always close the client socket
                try:
                    client_socket.close()
                except Exception:
                    pass
                self.get_logger().info(f'Closed connection with {client_address}')

    def destroy(self):
        """
        Cleanup the server socket when shutting down.
        """
        self.get_logger().info('Shutting down socket server')
        self.server_socket.close()
        super().destroy_node()


def main(args=None):
    rclpy.init(args=args)
    node = SocketBridgeNode()

    try:
        # Keep the node alive to process ROS callbacks
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info('Keyboard interrupt received, shutting down')
    finally:
        # Clean up sockets and destroy the node
        node.destroy()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
