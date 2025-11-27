import asyncio
import requests
from listing_2_16 import async_timed

@async_timed()
async def get_example_status() -> int:
    return requests.get('https://example.com').status_code # sync library requests doesn't allow to give up control

@async_timed()
async def main():
    task_1 = asyncio.create_task(get_example_status())
    task_2 = asyncio.create_task(get_example_status())
    task_3 = asyncio.create_task(get_example_status())

    await task_1
    await task_2
    await task_3

asyncio.run(main())

# Because requests is synchronous library, we can't get benefits of async tasks and the code is executed synchronously
# starting <function main at 0x000001D22993EDE0> with args () kwargs {}
# starting <function get_example_status at 0x000001D22993EC00> with args () kwargs {}
# finished <function get_example_status at 0x000001D22993EC00> in 0.9603 s
# starting <function get_example_status at 0x000001D22993EC00> with args () kwargs {}
# finished <function get_example_status at 0x000001D22993EC00> in 0.9080 s
# starting <function get_example_status at 0x000001D22993EC00> with args () kwargs {}
# finished <function get_example_status at 0x000001D22993EC00> in 0.7643 s
# finished <function main at 0x000001D22993EDE0> in 2.6332 s