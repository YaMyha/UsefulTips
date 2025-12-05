import asyncio
import aiohttp
import logging

from Concurrency_in_python_with_asyncio.chapter_04 import fetch_status
from Concurrency_in_python_with_asyncio.util.async_timer import async_timed

@async_timed()
async def main():
    async with aiohttp.ClientSession() as session:
        # we will have exception first
        fetchers = [asyncio.create_task(fetch_status(session, 'python://bad')),
                    asyncio.create_task(fetch_status(session, 'https://example.com', delay=3)),
                    asyncio.create_task(fetch_status(session, 'https://example.com', delay=3))] # second task will throw exception

        done, pending = await asyncio.wait(fetchers, return_when=asyncio.FIRST_EXCEPTION) # will return after first exception

        print(f'Done task count: {len(done)}')
        print(f'Pending task count: {len(pending)}')

        for done_task in done:
            # result = await done_task will throw an exception
            if done_task.exception() is None: # check if result of the task is exception
                print(done_task.result())
            else:
                logging.error("Request got an exception",
                              exc_info=done_task.exception())

        for pending_task in pending:
            pending_task.cancel()

asyncio.run(main())

# starting <function main at 0x000001B05196F2E0> with args () {}
# starting <function fetch_status at 0x000001B05196D080> with args (<aiohttp.client.ClientSession object at 0x000001B050CA67B0>, 'python://bad') {}
# starting <function fetch_status at 0x000001B05196D080> with args (<aiohttp.client.ClientSession object at 0x000001B050CA67B0>, 'https://example.com') {'delay': 3}
# starting <function fetch_status at 0x000001B05196D080> with args (<aiohttp.client.ClientSession object at 0x000001B050CA67B0>, 'https://example.com') {'delay': 3}
# finished <function fetch_status at 0x000001B05196D080> in 0.0001 second(s)
# Done task count: 1
# Pending task count: 2
# finished <function fetch_status at 0x000001B05196D080> in 0.0016 second(s)
# finished <function fetch_status at 0x000001B05196D080> in 0.0016 second(s)
# finished <function main at 0x000001B05196F2E0> in 0.0018 second(s)
# ERROR:root:Request got an exception
# Traceback (most recent call last):
#   File "C:\Users\Karina\PycharmProjects\UsefulTips\Concurrency_in_python_with_asyncio\util\async_timer.py", line 13, in wrapped
#     return await func(*args, **kwargs)
#            ^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "C:\Users\Karina\PycharmProjects\UsefulTips\Concurrency_in_python_with_asyncio\chapter_04\__init__.py", line 12, in fetch_status
#     async with session.get(url) as result:
#                ~~~~~~~~~~~^^^^^
#   File "C:\Users\Karina\PycharmProjects\UsefulTips\.venv\Lib\site-packages\aiohttp\client.py", line 1510, in __aenter__
#     self._resp: _RetType = await self._coro
#                            ^^^^^^^^^^^^^^^^
#   File "C:\Users\Karina\PycharmProjects\UsefulTips\.venv\Lib\site-packages\aiohttp\client.py", line 558, in _request
#     raise NonHttpUrlClientError(url)
# aiohttp.client_exceptions.NonHttpUrlClientError: python://bad