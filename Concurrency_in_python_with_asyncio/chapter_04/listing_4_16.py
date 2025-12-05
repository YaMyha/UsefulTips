import asyncio
import aiohttp

from Concurrency_in_python_with_asyncio.chapter_04 import fetch_status

async def main():
    async with aiohttp.ClientSession() as session:
        api_a = asyncio.create_task(fetch_status(session, 'https://www.example.com'))
        api_b = asyncio.create_task(fetch_status(session, 'https://www.example.com', delay=2))


        done, pending = await asyncio.wait([api_a, api_b], timeout=1)

        for task in pending: # we get api_b in pending and cancel it
            if task is api_b:
                print('API B too slow, cancelling')
                task.cancel()

asyncio.run(main())