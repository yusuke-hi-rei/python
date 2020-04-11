from asyncio import *

flg = {}

# fn
def fn(id, n):
    n += 1
    print(id + ": num=[" + str(n) + "]")

# finish
def finish():
    res = True
    vals = flg.values()
    for val in vals:
        if val == False:
            res = False
    if res:
        loop.stop()

# fisrt_fn
async def first_fn(nm, cnt, dy):
    flg[nm] = False
    for n in range(cnt):
        await sleep(dy)
        fn(nm, n)
    flg[nm] = True
    print("*** " + nm + " is finished. ***")
    finish()

# Get event loop
loop = get_event_loop()

ensure_future(first_fn("first", 5, 1))
ensure_future(first_fn("secound", 5, 1.5))
ensure_future(first_fn("third", 5, 2.5))

try:
    # "run_forever" keeps moving without end.
    loop.run_forever()
finally:
    loop.close()
