# Import all elements in a module
from math import *

print("----ABS, FABS----")
num = -123
print(abs(num))
print(fabs(num))

# round up
print("----Round up----")
num = 123.45
print(ceil(num))

# devaluation
print("----Devaluation----")
print(floor(num))


# Surplus
print("----Surplus----")
num1 = -10
num2 = 3
print(num1 % num2)
print("If there is a minus, % cannot be used.")

print(fmod(num1, num2))

# Find the sum
print("----SUM, FSUM----")
n = 0.1
lst = [n, n, n, n, n, n, n, n, n, n]
total1 = sum(lst)
total2 = fsum(lst)
print(total1)
print(total2)
