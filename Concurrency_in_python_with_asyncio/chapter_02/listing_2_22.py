import asyncio
from listing_2_17 import delay

def call_later():
    print("I'm being called in the future!")

async def main():
    loop = asyncio.get_running_loop() # get current event loop
    loop.call_soon(call_later) # set a timer that on the next control release this function will start and it will be executed as sync function
    await delay(1)

asyncio.run(main())

# Output
# We skip call_later and go to await delay()
# starting <function delay at 0x000001C02D7FE0C0> with args (1,) kwargs {}
# sleeping for 1 seconds
# delay gives up control and call_later is called as sync func
# I'm being called in the future!
# call_later finished and gave up
# we return to delay func
# finished sleeping for 1 seconds
# finished <function delay at 0x000001C02D7FE0C0> in 1.0031 s