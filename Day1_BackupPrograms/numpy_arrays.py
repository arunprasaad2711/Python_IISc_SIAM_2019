"""
Program to use numpy arrays.
"""

import numpy as np

l = [5, 7, 9]
t = (5, 7, 9.7)

a = np.array(l)
b = np.array(t)

print(type(l))
print(type(t))
print(type(a))
print(type(b))
print(np.dtype(a[2]))
print(np.dtype(b[1]))
