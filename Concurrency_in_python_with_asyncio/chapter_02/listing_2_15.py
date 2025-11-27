from asyncio import Future
import asyncio

def make_request() -> Future:
    """
    Create future and task to change it.
    :return: future
    """
    future = Future()
    asyncio.create_task(set_future_value(future))
    return future

async def set_future_value(future) -> None:
    """
    Async change of input future
    """
    await asyncio.sleep(1)
    future.set_result(42)

async def main() -> None:
    future = make_request() # get future that will be changed asynchronously
    print(f'Is the future done? {future.done()}') # false, 1 s hasn't passed yet
    value = await future # wait until future is set
    print(f'Is the future done? {future.done()}') # awaited future, now it's done
    print(value) # print value of the future

asyncio.run(main())

# Output
# Is the future done? False
# Is the future done? True
# 42