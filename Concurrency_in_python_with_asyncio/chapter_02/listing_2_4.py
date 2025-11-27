import asyncio
async def add_one(number: int) -> int:
    return number + 1

async def main() -> None:
    one_plus_one = await add_one(1)
    two_plus_one = await add_one(2)

    print(one_plus_one)
    print(two_plus_one)

asyncio.run(main())

# Output
# 2
# 2

# Now we throw main into event cycle
# It starts coroutine main
# In main it goes to 1st await and waits for its completion, but it doesn't work on 2nd add_one because it's not added to event cycle yet
# So there's no speed gain
# To achieve speed gain we need to make tasks from it