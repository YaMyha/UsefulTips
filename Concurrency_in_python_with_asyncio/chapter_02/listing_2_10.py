import asyncio
import time
from listing_2_6 import delay

async def hello_every_second():
    for i in range(3):
        await asyncio.sleep(1)
        print(f"{time.strftime("%H:%M:%S", time.localtime())} I'm running other code while I'm waiting")


async def main():
    # creating tasks
    first_delay = asyncio.create_task(delay(3))
    second_delay = asyncio.create_task(delay(3))

    await hello_every_second()
    await first_delay
    await second_delay

asyncio.run(main())

# Output
# First created tasks start to work and give up control
# 11:59:09 sleeping for 3 seconds
# 11:59:09 sleeping for 3 seconds
# hello every second starts executing and sleeps for a second
# in a second it writes message
# 11:59:10 I'm running other code while I'm waiting
# writes again, other tasks are still sleeping
# 11:59:11 I'm running other code while I'm waiting
# delays finished sleeping
# 11:59:12 finished sleeping for 3 seconds
# 11:59:12 finished sleeping for 3 seconds
# 11:59:12 I'm running other code while I'm waiting
