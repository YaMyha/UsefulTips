# In this example we can observe how cpu bound operations take control for all the time they work
import asyncio
from listing_2_16 import async_timed
from listing_2_17 import delay

@async_timed()
async def cpu_bound_work() -> int:
    counter = 0
    for i in range(100000):
        counter += 1
    return counter

@async_timed()
async def main():
    task_one = asyncio.create_task(cpu_bound_work())
    task_two = asyncio.create_task(cpu_bound_work())
    delay_task = asyncio.create_task(delay(4))

    await task_one
    await task_two
    await delay_task

asyncio.run(main())

# Output
# Start main
# starting <function main at 0x0000019425312200> with args () kwargs {}
# Start cpu bound
# starting <function cpu_bound_work at 0x0000019425311E40> with args () kwargs {}
# Finished cpu bound(no task switch)
# finished <function cpu_bound_work at 0x0000019425311E40> in 0.0026 s
# Start 2nd cpu_bound
# starting <function cpu_bound_work at 0x0000019425311E40> with args () kwargs {}
# Finished 2nd cpu_bound
# finished <function cpu_bound_work at 0x0000019425311E40> in 0.0037 s
# Start coroutine
# starting <function delay at 0x0000019425312020> with args (4,) kwargs {}
# sleeping for 4 seconds
# finished sleeping for 4 seconds
# finished <function delay at 0x0000019425312020> in 4.0015 s
# Finished main after sum(time_of_1st_cpu, time_of_2nd_cpu, time_delay)
# finished <function main at 0x0000019425312200> in 4.0080 s