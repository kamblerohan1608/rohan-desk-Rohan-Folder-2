import numpy as np
import sys

# array consumes less memory than list

ls = list(range(1000))
print(ls)

arr = np.arange(1000)
print(arr)

m = sys.getsizeof(ls[0])
print(m)
ls_size  = m * (len(ls))
print(ls_size)
print(arr.itemsize)
arr_size = arr.size * arr.itemsize
print(arr_size)