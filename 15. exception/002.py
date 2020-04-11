#!
#! Exceptions. raise
#!

num = input("input value: ")

try:
    n = int(num)
except ValueError:
    if n == "":
        print("......")
        n = 1
    else:
        raise
result = n * n

print(str(result))
