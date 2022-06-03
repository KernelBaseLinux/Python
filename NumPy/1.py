import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6,44,55])

newarr = np.array_split(arr, 90)

print(newarr)
