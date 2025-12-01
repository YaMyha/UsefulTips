import asyncio
from asyncio import AbstractEventLoop
import socket
import logging
import signal
from typing import List


async def echo(connection: socket,
               loop: AbstractEventLoop) -> None:
    """
    Coroutine that accepts connections and echoes their messages
    """
    try:
        while data := await loop.sock_recv(connection, 1024):
            print('Got data!')
            if data == b'boom\r\n': # key phrase for boom
                raise Exception("Unexpected network error")
            await loop.sock_sendall(connection, data)
    except Exception as e:
        logging.error(e)
    finally:
        connection.close()

echo_tasks = []

async def connection_listener(server_socket: socket,
                              loop: AbstractEventLoop) -> None:
    """
    Coroutine that accepts connections and makes tasks for them
    """
    while True:
        connection, address = await loop.sock_accept(server_socket)
        connection.setblocking(False)
        print(f"Got a connection from {address}")
        echo_task = asyncio.create_task(echo(connection, loop))
        echo_tasks.append(echo_task)


# custom systemExit
class GracefulExit(SystemExit):
    pass

def shutdown():
    raise GracefulExit()

async def close_echo_tasks(echo_tasks: List[asyncio.Task]):
    waiters = [asyncio.wait_for(task, 2) for task in echo_tasks] # give 2 seconds to tasks to finish
    for task in waiters:
        try:
            await task # get results of tasks
        except asyncio.exceptions.TimeoutError:
            pass


async def main():
    server_socket = socket.socket()
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server_address = ('127.0.0.1', 8000)
    server_socket.bind(server_address)
    server_socket.setblocking(False)
    server_socket.listen()

    for signame in {'SIGINT', 'SIGTERM'}:
        loop.add_signal_handler(getattr(signal, signame), shutdown)
    await connection_listener(server_socket, loop)


loop = asyncio.new_event_loop()

try:
    loop.run_until_complete(main()) # main is eternal loop
except GracefulExit: # if use hotkeys to shut down all
    loop.run_until_complete(close_echo_tasks(echo_tasks)) # wait for 2 s to finish echo tasks in the list(we will loose tasks that were added in this 2 s gap) and close loop
finally:
    loop.close()
