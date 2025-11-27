# Coroutine is a function that gives up control in await spots and able to continue execution after awaited operation

async def my_coroutine() -> None: # in annotation we write None, but it's semi truth because it returns coroutine object which has to be awaited
    print('Hello world')