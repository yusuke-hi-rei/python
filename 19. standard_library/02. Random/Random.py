# Import all elements in a module
from random import *

print(random())

print(randrange(10))

print(randrange(100, 200))


data = ["one", "two", "three", "four", "five"]

shuffle(data)
print(data)

item = choice(data)
print(item)

res = sample(data, 3)
print(res)

