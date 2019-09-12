import numpy as np  # Importing Numpy

# Getting started with Numpy

list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 7, 8]
# Print array with Numpy
# print np.array(list1)  # print 1-dimensional array

arr = np.array([list1, list2])

# print arr  # print multi-dimensional array with numpy

# print arr.shape  # use to find the shape of an array

# print arr.dtype  # use to find the datatypes of the members of the array
# newarr = np.zeros(5)
# newarr = np.ones([5,5])
# newarr = np.empty(5)
arange_arr = np.arange(5, 50, 3)  # use to create an array of evenly spaced values within an interval of start,
# stop with a step value. (e.g start = 5, stop = 50, step = 3)

print(arange_arr)
