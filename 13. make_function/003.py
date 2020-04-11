#!
#! Make function.
#!

def makeList(*arg):
  data = {}
  n = 0
  total = 0
  for num in arg:
    data[n] = num
    n += 1
    total += num
  else:
    data["total"] = total
  return data

data = makeList(98, 76, 54, 32)
print(data)
