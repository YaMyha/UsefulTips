import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 8080))
server_socket.listen()
server_socket.setblocking(False) # make socket non-blocking(it returns control immediately)

connections = []

try:
    while True:
        connection, client_address = server_socket.accept() # will return BlockingIOError if there are no incoming connections
        connection.setblocking(False)
        print(f'I got a connection from {client_address}!')
        connections.append(connection)

        for connection in connections:
            buffer = b''

            while buffer[-2:] != b'\r\n':
                data = connection.recv(2)
                if not data:
                    break
                else:
                    print(f'I got data: {data}!')
                    buffer += data

            print(f"All the data is: {buffer}")

            connection.send(buffer)
finally:
    server_socket.close()