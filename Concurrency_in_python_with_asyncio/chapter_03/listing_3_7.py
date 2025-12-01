import selectors
import socket
from selectors import SelectorKey
from typing import List, Tuple

selector = selectors.DefaultSelector() # chooses the most appropriate mechanism(linux -> epoll, macOS -> kqueue, win -> select)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_address = ('127.0.0.1', 8080)
server_socket.setblocking(False)
server_socket.bind(server_address)
server_socket.listen()

selector.register(server_socket, selectors.EVENT_READ) # signals if server socket received a message

while True:
    events: List[Tuple[SelectorKey, int]] = selector.select(timeout=1) # selector returns list of events every second [(SelectorKey, EVENT_TYPE), ...]

    if len(events) == 0:
        print('No events, waiting a bit more!')

    for event, _ in events:
        event_socket = event.fileobj # it is the socket

        if event_socket == server_socket: # if event came from server_socket -> new client connected
            connection, address = server_socket.accept()
            connection.setblocking(False)
            print(f'I got a connection from {address}')
            selector.register(connection, selectors.EVENT_READ) # signals if client socket received a message
        else: # data came from client
            data = event_socket.recv(1024)
            print(f"I got some data: {data}")
            event_socket.send(data)