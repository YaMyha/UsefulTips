import asyncio
from listing_2_6 import delay

async def main():
    # Creating tasks for delay and they start to work the same moment they are created
    sleep_for_three = asyncio.create_task(delay(3))
    sleep_again = asyncio.create_task(delay(3))
    sleep_once_more = asyncio.create_task(delay(3))

    # Waiting for results
    await sleep_for_three
    await sleep_again
    await sleep_once_more

asyncio.run(main())

# Output
# sleeping for 3 seconds
# sleeping for 3 seconds
# sleeping for 3 seconds
# finished sleeping for 3 seconds
# finished sleeping for 3 seconds
# finished sleeping for 3 seconds