import asyncio
import socket
from types import TracebackType
from typing import Optional, Type


class ConnectedSocket:
    def __init__(self, server_socket):
        self._connection = None
        self._server_socket = server_socket

    async def __aenter__(self): # runs if class is used as async context manager
        # it takes server_socket and asynchronously accepts connections
        print('Entering context manager, waiting for  connection')
        loop = asyncio.get_event_loop()
        connection, address = await loop.sock_accept(self._server_socket)
        self._connection = connection
        print('Accepted a connection')
        return self._connection

    async def __aexit__(self,
                        exc_type: Optional[Type[BaseException]],
                        exc_val: Optional[BaseException],
                        exc_tb: Optional[TracebackType]):
        # async closing of connection
        print('Exiting context manager')
        self._connection.close()
        print('Closed connection')


async def main():
    loop = asyncio.get_event_loop()

    server_socket = socket.socket()
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_address = ("127.0.0.1", 8000)
    server_socket.bind(server_address)
    server_socket.setblocking(False)
    server_socket.listen()

    async with ConnectedSocket(server_socket) as conn: # use ConnectedSocket as async context manager, it gives us full control of opening/closing connections without risks of forgetting
        data = await loop.sock_recv(conn, 1024)
        print(data)


asyncio.run(main())
