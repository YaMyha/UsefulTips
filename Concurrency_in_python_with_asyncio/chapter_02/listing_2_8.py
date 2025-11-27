import asyncio
from listing_2_6 import delay

async def main():
    sleep_for_three = asyncio.create_task(delay(3)) # creating task and it starts working immediately
    print(type(sleep_for_three)) # type Task

    result = await sleep_for_three # here we fetch result of the task, but it's already worked
    print(result)

asyncio.run(main())

# Output
# <class '_asyncio.Task'>
# sleeping for 3 seconds
# finished sleeping for 3 seconds
# 3

