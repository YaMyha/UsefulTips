import socket # library for low-level work with sockets

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # create socket AF_INET - IPv4, SOCK_STREAM - TCP
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # settings of the socket, SO_REUSEADDR - allows restart server even if port is in TIME_WAIT
# What is TIME_WAIT?
# When one side closes connection first, it goes to TIME_WAIT state approximately for 2xMSL(usually 1-4 minutes depending on OS)
# In this state:
# - Port is busy
# - OS waits for:
# - every old packages to disappear from network
# - 2nd side is able to get FIN/ACK if 1st side send it again(FIN - finish, it means "I stopped sending data. Closing my own side of connection", ACK - acknowledgement. It means "I got your message, all good")
# Generally, TIME_WAIT exists to avoid collision of old and new connections on the same IP+port

server_address = ('127.0.0.1', 8000)
server_socket.bind(server_address) # bind socket and host+port
server_socket.listen()

connection, client_address = server_socket.accept() # accept client connection
print(f'I got a connection from {client_address}!')
server_socket.close() # close socket