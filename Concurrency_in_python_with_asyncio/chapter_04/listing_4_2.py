import asyncio
import aiohttp
from aiohttp import ClientSession

from Concurrency_in_python_with_asyncio.util.async_timer import async_timed


@async_timed()
async def fetch_status(session: ClientSession, url: str) -> int:
    async with session.get(url) as response: # send get request to url and return status
        return response.status

@async_timed()
async def main():
    async with aiohttp.ClientSession() as session: # create client session, it will open/close it automatically
        url = 'https://www.example.com/'
        status = await fetch_status(session, url) # asyncly fetch_status
        print(f'Status for {url} was {status}')

asyncio.run(main())