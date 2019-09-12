import numpy as np

# saving single arrays
arr = np.arange(10)
print arr

np.save('saved_array.npy', arr)  # it will create a new file called saved_array.npy

new_array = np.load('saved_array.npy')  # np.load is a function used to load the save array back
print new_array

# save multiple arrays
arr1 = np.arange(25)
arr2 = np.arange(40)

np.savez('saved_archive.npz', x=arr1, y=arr2)

load_archive = np.load('saved_archive.npz')
print 'load_archive of x is'
print load_archive['x']

print 'load_archive of y is'
print load_archive['y']

# save to txt file

np.savetxt('notepadfile.txt', arr1, delimiter=',')

# loading txt files

load_txt_file = np.loadtxt('notepadfile.txt', delimiter=',')
print 'load txt file is'
print load_txt_file
