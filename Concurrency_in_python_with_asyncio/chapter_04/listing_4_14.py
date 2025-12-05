import asyncio
import aiohttp

from Concurrency_in_python_with_asyncio.chapter_04 import fetch_status
from Concurrency_in_python_with_asyncio.util.async_timer import async_timed

@async_timed()
async def main():
    async with aiohttp.ClientSession() as session:
        url = 'https://www.example.com/'
        pending = [asyncio.create_task(fetch_status(session, url)) for _ in range(3)]

        while pending:
            done, pending = await asyncio.wait(pending, return_when=asyncio.FIRST_COMPLETED) # it will return first completed

            print(f'Done task count: {len(done)}')
            print(f'Pending task count: {len(pending)}')

            for done_task in done:
                print(await done_task)

asyncio.run(main())

# starting <function main at 0x0000022CEC11E0C0> with args () {}
# starting <function fetch_status at 0x0000022CEC11CFE0> with args (<aiohttp.client.ClientSession object at 0x0000022CEB4D6660>, 'https://www.example.com/') {}
# starting <function fetch_status at 0x0000022CEC11CFE0> with args (<aiohttp.client.ClientSession object at 0x0000022CEB4D6660>, 'https://www.example.com/') {}
# starting <function fetch_status at 0x0000022CEC11CFE0> with args (<aiohttp.client.ClientSession object at 0x0000022CEB4D6660>, 'https://www.example.com/') {}
# finished <function fetch_status at 0x0000022CEC11CFE0> in 0.1813 second(s)
# RETURNED 1ST
# Done task count: 1
# Pending task count: 2 # 2 PENDING
# 200
# OTHER TASKS WORKED ON THE BACKGROUND
# finished <function fetch_status at 0x0000022CEC11CFE0> in 0.2296 second(s)
# finished <function fetch_status at 0x0000022CEC11CFE0> in 0.2297 second(s)
# NEXT WAITFOR RETURNS OTHER TASKS
# Done task count: 2
# Pending task count: 0
# 200
# 200
# finished <function main at 0x0000022CEC11E0C0> in 0.2310 second(s)