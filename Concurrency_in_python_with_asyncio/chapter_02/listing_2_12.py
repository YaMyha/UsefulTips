import asyncio
from listing_2_6 import delay

async def main():
    delay_task = asyncio.create_task(delay(2))
    try:
        # here we use wait_for, which allows us to set timeout for task
        result = await asyncio.wait_for(delay_task, timeout=1)
        print(result)
    except asyncio.exceptions.TimeoutError:
        print('Got a timeout!')
        print(f'Was the task cancelled? {delay_task.cancelled()}')

asyncio.run(main())