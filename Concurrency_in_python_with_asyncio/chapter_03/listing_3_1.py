import socket # library for low-level work with sockets

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # create socket
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # settings of the socket

server_address = ('127.0.0.1', 8000)
server_socket.bind(server_address) # bind socket and host+port
server_socket.listen()

connection, client_address = server_socket.accept() # accept client connection
print(f'I got a connection from {client_address}!')
server_socket.close() # close socket