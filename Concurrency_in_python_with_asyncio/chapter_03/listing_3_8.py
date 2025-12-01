import asyncio
import socket
from asyncio import AbstractEventLoop

async def echo(connection: socket,
               loop: AbstractEventLoop) -> None:
    while data := await loop.sock_recv(connection, 1024): # async func, non-blocking. If sock_recv returns b'', then it means the client closed the connection
        await loop.sock_sendall(connection, data) # async func


async def listen_for_connection(server_socket: socket.socket,
                                loop: AbstractEventLoop):
    while True:
        connection, address = await loop.sock_accept(server_socket) # async func, non-blocking
        connection.setblocking(False)
        print(f'Got a connection from {address}')
        asyncio.create_task(echo(connection, loop)) # start echo task that echoes incoming data until the connection is closed


async def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)

    server_address = ('127.0.0.1', 8000)
    server_socket.bind(server_address)
    server_socket.setblocking(False)

    await listen_for_connection(server_socket, asyncio.get_event_loop()) # background eternal task  accepting connections and creating processing tasks

asyncio.run(main())