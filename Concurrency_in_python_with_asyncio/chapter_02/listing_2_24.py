import asyncio
# I dunno why and how but we can set slow_callback_duration and in debug mode asyncio will log slow callbacks and coroutines
async def main():
    loop = asyncio.get_running_loop()
    loop.slow_callback_duration = .250

asyncio.run(main(), debug=True)