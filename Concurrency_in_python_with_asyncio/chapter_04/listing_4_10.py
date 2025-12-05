import asyncio
import aiohttp

from Concurrency_in_python_with_asyncio.chapter_04 import fetch_status
from Concurrency_in_python_with_asyncio.util.async_timer import async_timed

@async_timed()
async def main():
    async with aiohttp.ClientSession() as session:
        fetchers = [asyncio.create_task(fetch_status(session, 'https://example.com')),
                    asyncio.create_task(fetch_status(session, 'https://example.com'))]

        done, pending = await asyncio.wait(fetchers) # it will wait all the tasks to be completed

        print(f'Done task count: {len(done)}')
        print(f'Pending task count: {len(pending)}')

        for done_task in done:
            result = await done_task
            print(result)

asyncio.run(main())

# starting <function main at 0x000001853A46E020> with args () {}
# starting <function fetch_status at 0x000001853A46CF40> with args (<aiohttp.client.ClientSession object at 0x00000185397E6660>, 'https://example.com') {}
# starting <function fetch_status at 0x000001853A46CF40> with args (<aiohttp.client.ClientSession object at 0x00000185397E6660>, 'https://example.com') {}
# finished <function fetch_status at 0x000001853A46CF40> in 0.4702 second(s)
# finished <function fetch_status at 0x000001853A46CF40> in 0.6636 second(s)
# Done task count: 2
# Pending task count: 0
# 200
# 200
# finished <function main at 0x000001853A46E020> in 0.6753 second(s)