import asyncio
from listing_2_16 import async_timed

@async_timed()
async def delay(delay_seconds: int) -> int:
    print(f'sleeping for {delay_seconds} seconds')
    await asyncio.sleep(delay_seconds)
    print(f'finished sleeping for {delay_seconds} seconds')
    return delay_seconds

@async_timed()
async def main():
    task_one = asyncio.create_task(delay(2))
    task_two = asyncio.create_task(delay(3))

    await task_one
    await task_two

if __name__ == '__main__':
    asyncio.run(main())

# Output
# Step into async_timed for main
# starting <function main at 0x000002CA2FC31EE0> with args () kwargs {}
# Start task and step into async_timed for delay(2)
# starting <function delay at 0x000002CA2FBE1E40> with args (2,) kwargs {}
# sleeping for 2 seconds
# Start task and step into async_timed for delay(3)
# starting <function delay at 0x000002CA2FBE1E40> with args (3,) kwargs {}
# sleeping for 3 seconds
# finished sleeping for 2 seconds
# delay(2) finished after 2 seconds + some time for calculating time
# finished <function delay at 0x000002CA2FBE1E40> in 2.0148 s
# finished sleeping for 3 seconds
# finished <function delay at 0x000002CA2FBE1E40> in 3.0025 s
# delay(2) finished after 3 seconds + some time for calculating time
# finished <function main at 0x000002CA2FC31EE0> in 3.0031 s
# main finished after 3 seconds + some time for calculating time
