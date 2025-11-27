import asyncio

async def coroutine_add_one(number: int) -> int:
    return number + 1

result = asyncio.run(coroutine_add_one(1))

print(result)

# Output
# 2

# we run event cycle at 6th line and add our coroutine to it so result is result of finished coroutine