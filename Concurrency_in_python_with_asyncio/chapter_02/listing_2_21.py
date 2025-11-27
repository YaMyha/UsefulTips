import asyncio
from asyncio import new_event_loop


async def main():
    await asyncio.sleep(1)

loop = new_event_loop() # creating new event loop

try:
    loop.run_until_complete(main()) # passing main coroutine to new event loop
finally:
    loop.close() # close loop after all