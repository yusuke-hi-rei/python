#!
#! for.
#!

data = {"kokugo": 98, "suugaku": 82, "rika": 67, "shakai": 59, "eigo": 65}
total = 0

for k in data:
    if k in {"kokugo", "suugaku", "eigo"}:
        print(k + ": " + str(data[k]))
    else:
        continue
    # print(k + ":" + str(data[k]))
    total += data[k]
else:
   print("--[else] is processed when exiting a [for] statement.--") 

average = total // len(data)
msg = "total: " + str(total) + " average: " + str(average)
print(msg)

#!
#! while.
#!

num = 12345
n = 2
result = []

while n <= num // 2:
    if num % n == 0:
        result += [n]
    n += 1
print(str(num) + " : divisor.")
print(result)
