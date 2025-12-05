import asyncio
import aiohttp

from Concurrency_in_python_with_asyncio.chapter_04 import fetch_status
from Concurrency_in_python_with_asyncio.util.async_timer import async_timed

@async_timed()
async def main():
    async with aiohttp.ClientSession() as session:
        url = 'https://www.example.com/'
        pending = [asyncio.create_task(fetch_status(session, url)),
                   asyncio.create_task(fetch_status(session, url)),
                   asyncio.create_task(fetch_status(session, url, delay=3))]

        while pending:
            done, pending = await asyncio.wait(pending, timeout=1) # wait for 1 second and return

            print(f'Done task count: {len(done)}')
            print(f'Pending task count: {len(pending)}')

            for done_task in done:

                print(await done_task)

asyncio.run(main())

# starting <function main at 0x000001763CBEE020> with args () {}
# starting <function fetch_status at 0x000001763CBECF40> with args (<aiohttp.client.ClientSession object at 0x000001763BFA6660>, 'https://www.example.com/') {}
# starting <function fetch_status at 0x000001763CBECF40> with args (<aiohttp.client.ClientSession object at 0x000001763BFA6660>, 'https://www.example.com/') {}
# starting <function fetch_status at 0x000001763CBECF40> with args (<aiohttp.client.ClientSession object at 0x000001763BFA6660>, 'https://www.example.com/') {'delay': 3}
# finished <function fetch_status at 0x000001763CBECF40> in 0.1441 second(s)
# finished <function fetch_status at 0x000001763CBECF40> in 0.1469 second(s)
# 2 TASKS FINISHED IN 1 S
# Done task count: 2
# Pending task count: 1
# 200
# 200
# NEXT ITERATION
# Done task count: 0
# Pending task count: 1 # 3 TASK STILL WORKING
# finished <function fetch_status at 0x000001763CBECF40> in 3.0329 second(s)
# NEXT ITERATION
# Done task count: 1 # 3RD TASK DONE
# Pending task count: 0
# 200
# finished <function main at 0x000001763CBEE020> in 3.0349 second(s)