async def coroutine_add_one(number: int) -> int:
    return number + 1

def add_one(number: int) -> int:
    return number + 1

function_result = add_one(1)
coroutine_result = coroutine_add_one(1)

print(f'Function result is {function_result} and the type is {type(function_result)}')
print(f'Function result is {coroutine_result} and the type is {type(coroutine_result)}')

# Output
# <sys>:0: RuntimeWarning: coroutine 'coroutine_add_one' was never awaited
# Function resilt is 2 and the type is <class 'int'>
# Function resilt is <coroutine object coroutine_add_one at 0x000001D204235C00> and the type is <class 'coroutine'>

# Plain function returns int as expected
# Async function return coroutine object and since it's not awaited we got warning