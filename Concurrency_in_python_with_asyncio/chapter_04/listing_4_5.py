import asyncio

from Concurrency_in_python_with_asyncio.util.async_timer import async_timed
from Concurrency_in_python_with_asyncio.util.delay_functions import delay


@async_timed()
async def main() -> None:
    delay_times = [3, 3, 3]
    tasks = [asyncio.create_task(delay(seconds)) for seconds in delay_times]
    [await task for task in tasks] # receiving results from tasks

asyncio.run(main())