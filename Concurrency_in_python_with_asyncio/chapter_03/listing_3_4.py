import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 8080))
server_socket.listen()
server_socket.setblocking(False) # make socket non-blocking(it returns control immediately)