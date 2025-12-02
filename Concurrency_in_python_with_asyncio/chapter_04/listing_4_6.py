import asyncio
import aiohttp

from Concurrency_in_python_with_asyncio.chapter_04 import fetch_status
from Concurrency_in_python_with_asyncio.util.async_timer import async_timed


@async_timed()
async def main():
    async with aiohttp.ClientSession() as session:
        urls = ['https://example.com' for _ in range(1000)]
        requests = [fetch_status(session, url) for url in urls]
        status_codes = await asyncio.gather(*requests) # creates tasks from all the coroutines and waits for them all completed
        print(status_codes)

asyncio.run(main())