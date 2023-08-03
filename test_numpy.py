# from numpy import *
# # install test
# print(eye(4))

# #
# a = array([1, 2, 3, 4])
# print(a)
# print(a[1])

# #
# student = dtype([('name','S20'), ('age', 'i1'), ('marks', 'f4')])
# a = array([('abc', 21, 50),('xyz', 18, 75)], dtype = student)
# print(student)
# print(a['marks'])

import numpy as np

# arr = np.empty([3, 2], dtype = int)
# print(arr)

# x = np.zeros(5)
# print(x)

# a = np.arange(5.)
# print(a)

# b = np.linspace(1, 10)
# print(b)

a = np.arange(25).reshape(5, 5)
print(a)
# print(a[1:3, 1:3])

i = [1, 2, 4]
j = np.array([0, 2, 4])
print(a[i, :][:, j])
print(a[i, ...][..., j])
print(a[..., 1])
