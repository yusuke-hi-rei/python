#!
#! Tuple and Range.
#!

#!
#! tuple is Immutable.(Value cannot be changed)
#!
tp = (1, 10, 30, 40)
print(tp)

tp = (1, "abc", "ef", 40)
print(tp)

a = tp[1]
print(a)

tp2 = (1, 10) + (100, 200)
print(tp2)

#!
#! Range is Immutable.(Value cannot be changed)
#!

rg1 = range(10)
result = tuple(rg1)
print(result)

rg1 = range(10, 20)
result = tuple(rg1)
print(result)

rg1 = range(10, 20, 3)
result = list(rg1)
print(result)

