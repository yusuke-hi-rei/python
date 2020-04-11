from asyncio import *

def fn(n):
    print("fn: num=" + str(n))

async def first_fn():
    for n in range(5):
        await sleep(1)
        fn(n)

# Get event loop
loop = get_event_loop()
# Execute coroutine in event loop.
# run_until_complete: When the coroutine processing ends,
#                     the event loop automatically ends.
loop.run_until_complete(first_fn())
# Close the event loop.
loop.close()

