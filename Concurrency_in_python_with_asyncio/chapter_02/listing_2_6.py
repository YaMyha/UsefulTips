# Auxiliary func for sleeping
import asyncio
import time


async def delay(delay_seconds: int) -> int:
    print(f'{time.strftime("%H:%M:%S", time.localtime())} sleeping for {delay_seconds} seconds')
    await asyncio.sleep(delay_seconds)
    print(f'{time.strftime("%H:%M:%S", time.localtime())} finished sleeping for {delay_seconds} seconds')
    return delay_seconds