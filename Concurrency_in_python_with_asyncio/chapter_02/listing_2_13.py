import asyncio
from listing_2_6 import delay

# async def main():
#     task = asyncio.create_task(delay(10))
#
#     try:
#         result = await asyncio.wait_for(task, timeout=5)
#         print(result)
#     except asyncio.exceptions.TimeoutError:
#         print('Timed out!')
#         result = await task
#         # result = await task
#         # ^ ^ ^ ^ ^ ^ ^ ^ ^ ^
#         # asyncio.exceptions.CancelledError
#         # we get it because task was cancelled in wait_for
#         print(result)

async def main():
    task = asyncio.create_task(delay(10))

    try:
        result = await asyncio.wait_for(asyncio.shield(task), timeout=5) # this shield protects task from cancellation, and it continues to work
        print(result)
    except asyncio.exceptions.TimeoutError:
        print('Timed out!')
        result = await task
        print(result)

asyncio.run(main())

# Output
# 14:22:46 sleeping for 10 seconds
# Timed out!
# 14:22:56 finished sleeping for 10 seconds
# 10