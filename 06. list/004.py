#!
#! List operation.
#!

# Append list.
a = [10, 30, 50, 70]
a.append(80)
a.append(200)
print(a)

# Insert into list.
b = [10, 30, 50, 70]
b.insert(1, 100)
print(b)

# Remove value from list.
b.remove(30)
print(b)

# Remove from list.
c = b.index(50)
del b[c]
print(b)

# pop
d = b.pop()
print(d)
print(b)

# reverse
a = [10, 30, 50, 70]
a.reverse()
print(a)

# sort
a.sort()
print(a)

# sort
a.sort(reverse=True)
print(a)
