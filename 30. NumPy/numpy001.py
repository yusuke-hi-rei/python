#!
#! NumPy is a numerical calculation library of PYTHON.
#! - Using NumPy makes matrix calculations easy.

import numpy as np

print("### Initialize.")
a = np.array([1, 2, 3, 4, 5])
print(a)
print(type(a))

print("### Creating a two-dimensional array with NumPy.")
b = np.array([[1, 2, 3], [4, 5, 6]])
print(b)

print("### Other initialize.")
c = np.zeros(10);
d = np.zeros((3, 2));
print(c)
print(d)

print("### Check the number of dimensions of the array.")
a = np.array([[1, 2, 3], [4, 5, 6]])
print(a.shape)

a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(a.shape)

print("### Convert a 2D array to 1D.")
a = np.array([[1, 2, 3], [4, 5, 6]])
print("a: ", a)
b = a.flatten()
print("b: ", b)

print("### Arbitrarily change the number of array dimensions.")
a = np.array([[1, 2, 3], [4, 5, 6]])
print("a: ", a)
print("re: ", a.reshape(3, 2))


print("### Access the elements of the array.")
v = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
#! Get the 0th of the array.
a = v[0]
#! Get the first and subsequent elements of the array.
b = v[1:]
#! Get each 0th in the array.
c = v[: , 0] 
print("a: ", a)
print("b: ", b)
print("c: ", c)


