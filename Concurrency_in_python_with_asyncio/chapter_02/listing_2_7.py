import asyncio
from listing_2_6 import delay

async def add_one(number: int) -> int:
    return number + 1

async def hello_world_message() -> str:
    await delay(1)
    return 'hello world'

async def main() -> None:
    message = await hello_world_message()
    one_plus_one = await add_one(1)
    print(one_plus_one)
    print(message)

asyncio.run(main())

# Output
# sleeping for 1 seconds
# finished sleeping for 1 seconds
# 2
# hello world

# Sequent execution