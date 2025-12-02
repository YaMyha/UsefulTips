import asyncio

from Concurrency_in_python_with_asyncio.util.delay_functions import delay


async def main():
    results = await asyncio.gather(delay(3), delay(3))
    print(results)

asyncio.run(main())

# Output
# sleeping for 3 second(s)
# sleeping for 3 second(s)
# finished sleeping for 3 second(s)
# finished sleeping for 3 second(s)
# [3, 3]