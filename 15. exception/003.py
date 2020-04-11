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

if n == 0:
    raise ZeroDivisionError("division by zero.")

result = 100 / n

print(str(result))
