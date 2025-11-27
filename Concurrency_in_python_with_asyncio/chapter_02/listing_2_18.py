import asyncio
from listing_2_16 import async_timed

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

    await task_one
    await task_two

asyncio.run(main())

# Output
# starting <function main at 0x00000209446C1F80> with args () kwargs {}
# because cpu_bound_work don't use IO bound ops, event loop doesn't switch tasks and they are executed synchronously
# starting <function cpu_bound_work at 0x0000020944694040> with args () kwargs {}
# finished <function cpu_bound_work at 0x0000020944694040> in 0.0032 s
# starting <function cpu_bound_work at 0x0000020944694040> with args () kwargs {}
# finished <function cpu_bound_work at 0x0000020944694040> in 0.0038 s
# finished <function main at 0x00000209446C1F80> in 0.0073 s
# total time is a sum of time spent on both calculations