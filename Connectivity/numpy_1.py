
# Numpy Library

# Important library for scientific calculations.

# converting into array to operate on data

import numpy as np
ls = [1,2,3,4,5]

arr = np.array(ls)
print(ls)
print(arr)

print(arr.ndim)   # dimentions of array (1d,2d,3d)

print(arr.shape)   # defines shape in form of (rows,columns) i.e ((5,),(3,2),(3,3))

print(arr.size)    # returns number of elements 

print(arr.itemsize)    # returns size of the element

print (arr.dtype)     # returns type of data

arr = np.array([[1,1],[1,2],[1,3]])
print(arr)

print(arr.ndim)
print(arr.shape)
print(arr.size)

arr = np.array([[[1,1],[1,2],[1,3],[2,1],[2,2],[2,3]]])
print(arr)
print(arr.ndim)
print(arr.shape)
print(arr.size)

arr = np.arange(1,10)
print(arr)

arr = np.zeros(10)
print(arr)

arr = np.ones(10)
print(arr)

arr = np.arange(1,9)
print(arr)

arr1 =arr.reshape(2,2,2)
print(arr1)