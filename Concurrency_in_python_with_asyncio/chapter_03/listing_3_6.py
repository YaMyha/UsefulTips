import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 8080))
server_socket.listen()
server_socket.setblocking(False) # make socket non-blocking(it returns control immediately)

connections = []

try:
    while True:
        try:
            connection, client_address = server_socket.accept()
            connection.setblocking(False)
            print(f'I got a connection from {client_address}!')
            connections.append(connection)
        except BlockingIOError: # if no incoming connections handle BlockingIOError
            pass

        for connection in connections:
            try:
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
            except BlockingIOError:  # if no incoming data handle BlockingIOError
                pass
finally:
    server_socket.close()