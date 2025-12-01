import asyncio
from asyncio import AbstractEventLoop
import signal
from typing import Set

from Concurrency_in_python_with_asyncio.util.delay_functions import delay

# Not for WIndows, it doesn't have signals
def cancel_tasks():
    print('Got a SIGINT!')
    tasks: Set[asyncio.Task] = asyncio.all_tasks()
    print(f'Cancelling {len(tasks)} task(s).')
    [task.cancel() for task in tasks]

async def main():
    loop: AbstractEventLoop = asyncio.get_running_loop()

    loop.add_signal_handler(signal.SIGINT, cancel_tasks) # SIGINT - Ctrl+C from keyboard

    await delay(10)

asyncio.run(main())