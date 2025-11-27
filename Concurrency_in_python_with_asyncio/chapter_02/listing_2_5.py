import asyncio

async def hello_world_message() -> str:
    await asyncio.sleep(1)
    return 'Hello World!'

async def main() -> None:
    message = await hello_world_message()
    print(message)

asyncio.run(main())

# Output
# Hello World!
# This code wait 1 s and writes Hello World! to output
# We could use time when asyncio.sleep executes in other coroutine, but we have only one task to work