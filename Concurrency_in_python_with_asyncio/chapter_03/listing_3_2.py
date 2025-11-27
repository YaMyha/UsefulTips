import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # create socket
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # settings of the socket

server_address = ('127.0.0.1', 8000)
server_socket.bind(server_address) # bind socket and host+port
server_socket.listen()

try:
    connection, client_address = server_socket.accept()
    print(f'I got a connection from {client_address}!')

    # Add incoming data processing
    buffer = b''

    while buffer[-2:] != b'\r\n': # check if it's stop phrase
        data = connection.recv(2) # read 2 bytes
        if not data:
            break
        else:
            print(f'I got data: {data}!')
            buffer += data # add to buffer

    print(f'All the data is: {buffer}')
finally:
    server_socket.close()
