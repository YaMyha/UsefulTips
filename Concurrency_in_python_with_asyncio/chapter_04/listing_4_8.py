import asyncio
import aiohttp

from Concurrency_in_python_with_asyncio.chapter_04 import fetch_status
from Concurrency_in_python_with_asyncio.util.async_timer import async_timed


@async_timed()
async def main():
    async with aiohttp.ClientSession() as session:
        fetchers = [fetch_status(session, 'https://example.com', 1),
                    fetch_status(session, 'https://example.com', 1),
                    fetch_status(session, 'https://example.com', 10)]

        for finished_task in asyncio.as_completed(fetchers): # as_completed will spit out tasks in order of readiness
            print(await finished_task)

asyncio.run(main())