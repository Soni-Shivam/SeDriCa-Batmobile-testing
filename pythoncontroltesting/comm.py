import socket 

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host = '0.0.0.0'
port = 85
server_socket.bind ((host,port))
server_socket.listen ( 1)

print( "waiting for connection from jetson")
client_socket,client_address = server_socket.accept()

print (f"connection established with {client_address}")
message = client_socket.recv(1024).decode()
print(f"message received from {client_address} with msg {message} ")

server_socket.close()
