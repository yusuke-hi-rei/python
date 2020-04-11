# Import all elements in a module
from statistics import *
data = [98, 76, 54, 58, 69, 80, 47, 71, 61, 83]

print("---------average----------")
average = mean(data)
print(average)

print("---------median----------")
mid = median(data)
print(mid)

print("---------Population standard deviation(母標準偏差)----------")
valuePstdev = pstdev(data)
print(valuePstdev)

print("---------Sample standard deviation(標本標準偏差)----------")
valueStdev = stdev(data)
print(valueStdev)

print("---------result----------")
print("[偏差値 = 10 * (点数 - 平均点) / 標準偏差 + 50]")
result = []
for n in data:
    result += [10 * (n - average) // valueStdev + 50]

for i in range(len(data)):
    print(str(data[i]) + "\t" + str(result[i]))


