import numpy as np

arr = np.arange(0, 12)
# print arr[0:4]

arr[0:5] = 20  # From index of 0-5 replace it with 20
print arr

# Intresting thing & Important

arr2 = arr[0:6]

arr2[:] = 29  # all elements are modified

# print arr2
print arr

# Creating new array copy

arrcopy = arr.copy()
