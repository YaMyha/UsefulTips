import asyncio

from Concurrency_in_python_with_asyncio.util.async_timer import async_timed
from Concurrency_in_python_with_asyncio.util.delay_functions import delay


@async_timed()
async def main() -> None:
    delay_times = [3, 3, 3]
    [await asyncio.create_task(delay(seconds)) for seconds in delay_times]

asyncio.run(main())