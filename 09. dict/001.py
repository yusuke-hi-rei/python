#!
#! Dictionary.
#!

dc1 = {"a": 100, "b": 200, "c": 300}
a = dc1["a"]
print(a)

del dc1["a"]
print(dc1)


dc1 = {"a": 100, "b": 200, "c": 300}
a = list(dc1.keys())
print(a)

a = list(dc1.values())
print(a)

a = list(dc1.items())
print(a)
