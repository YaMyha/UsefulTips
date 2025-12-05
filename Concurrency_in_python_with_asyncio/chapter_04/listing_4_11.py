import asyncio
import aiohttp
import logging

from Concurrency_in_python_with_asyncio.chapter_04 import fetch_status
from Concurrency_in_python_with_asyncio.util.async_timer import async_timed

@async_timed()
async def main():
    async with aiohttp.ClientSession() as session:
        good_request = fetch_status(session, 'https://example.com')
        bad_request = fetch_status(session, 'python://bad')

        fetchers = [asyncio.create_task(good_request),
                    asyncio.create_task(bad_request)] # second task will throw exception

        done, pending = await asyncio.wait(fetchers)

        print(f'Done task count: {len(done)}')
        print(f'Pending task count: {len(pending)}')

        for done_task in done:
            # result = await done_task will throw an exception
            if done_task.exception() is None: # check if result of the task is exception
                print(done_task.result())
            else:
                logging.error("Request got an exception",
                              exc_info=done_task.exception())

asyncio.run(main())

# starting <function main at 0x000001316A8FE020> with args () {}
# starting <function fetch_status at 0x000001316A8FCF40> with args (<aiohttp.client.ClientSession object at 0x0000013169C667B0>, 'https://example.com') {}
# starting <function fetch_status at 0x000001316A8FCF40> with args (<aiohttp.client.ClientSession object at 0x0000013169C667B0>, 'python://bad') {}
# finished <function fetch_status at 0x000001316A8FCF40> in 0.0020 second(s)
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
# finished <function fetch_status at 0x000001316A8FCF40> in 0.6464 second(s)
# Done task count: 2
# Pending task count: 0
# 200
# finished <function main at 0x000001316A8FE020> in 0.6483 second(s)