import asyncio
import aiohttp
from aiohttp import ClientSession

async def fetch_status(session: ClientSession, url: str) -> int:
    ten_millis = aiohttp.ClientTimeout(total=0.01) # declare timeout object
    async with session.get(url, timeout=ten_millis) as response: # add timeout to request
        return response.status


async def main():
    session_timeout = aiohttp.ClientTimeout(total=1, connect=.1) # timeout for session, total - default for every request in this session, connect - for tcp connection establishment
    async with aiohttp.ClientSession(timeout=session_timeout) as session:
        await fetch_status(session, url="http://www.example.com/")


asyncio.run(main())
