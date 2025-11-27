import asyncio
from asyncio import CancelledError
from listing_2_6 import delay

async def main():
    long_task = asyncio.create_task(delay(10))

    seconds_elapsed = 0

    # Manual checking if task is done
    while not long_task.done():
        print('Task not finished. checking again in a second.')
        await asyncio.sleep(1)
        seconds_elapsed += 1

        # the task will be finished anyways because delay is 10 s and we cancel it in 5 s
        if seconds_elapsed == 5:
            long_task.cancel()

    try:
        # here we fetch result of the task that in our case is Error
        await long_task
    except CancelledError:
        print('Our task was cancelled!')

asyncio.run(main())