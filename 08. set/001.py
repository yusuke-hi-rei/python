#!
#! Set and Frozenset.
#!

#!
#! set is Mutable.(Value can be changed)
#!
st1 = {10, 20, 30}
st2 = {10, 30, 300}

a = st1 & st2
print(a)

b = st1 | st2
print(b)

st1.add(50)
print(st1)

st1.remove(50)
print(st1)

#!
#! frozenset is Immutable.(Value can not be changed)
#!
st1 = {10, 20, 30}
st2 = {10, 30, 300}

frset1 = frozenset(st1)
frset2 = frozenset(st2)


a = frset1 & frset2
print(a)

b = frset1 | frset2
print(b)

print(10 in frset1)

#! can not add.
#frset1.add(50)
#print(st1)

#! can not remove.
#frset1.remove(50)
#print(st1)
