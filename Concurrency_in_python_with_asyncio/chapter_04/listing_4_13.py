import asyncio
import aiohttp

from Concurrency_in_python_with_asyncio.chapter_04 import fetch_status
from Concurrency_in_python_with_asyncio.util.async_timer import async_timed

@async_timed()
async def main():
    async with aiohttp.ClientSession() as session:
        url = 'https://example.com'
        fetchers = [asyncio.create_task(fetch_status(session, url)),
                    asyncio.create_task(fetch_status(session, url)),
                    asyncio.create_task(fetch_status(session, url))]

        done, pending = await asyncio.wait(fetchers, return_when=asyncio.FIRST_COMPLETED)

        print(f'Done task count: {len(done)}') # only 1 task was completed
        print(f'Pending task count: {len(pending)}')

        for done_task in done:
            print(await done_task) # get result

asyncio.run(main())

# starting <function main at 0x000002C4C4B3E020> with args () {}
# starting <function fetch_status at 0x000002C4C4B3CF40> with args (<aiohttp.client.ClientSession object at 0x000002C4C3EF6660>, 'https://example.com') {}
# starting <function fetch_status at 0x000002C4C4B3CF40> with args (<aiohttp.client.ClientSession object at 0x000002C4C3EF6660>, 'https://example.com') {}
# starting <function fetch_status at 0x000002C4C4B3CF40> with args (<aiohttp.client.ClientSession object at 0x000002C4C3EF6660>, 'https://example.com') {}
# finished <function fetch_status at 0x000002C4C4B3CF40> in 0.4506 second(s)
# Done task count: 1
# Pending task count: 2
# 200
# finished <function main at 0x000002C4C4B3E020> in 0.4518 second(s)
# finished <function fetch_status at 0x000002C4C4B3CF40> in 0.4519 second(s)
# finished <function fetch_status at 0x000002C4C4B3CF40> in 0.4520 second(s)