import pandas as pd

'''
pandas.Series( data, index, dtype, copy)
***************************************
1.data
-------
data takes various forms like ndarray, list, constants

2.index
-------
Index values must be unique and hashable, same length as data. Default np.arrange(n) if no index is passed.

3.dtype
-------
dtype is for data type. If None, data type will be inferred

4.copy
-------
Copy data. Default False
'''
'''
a = ["Sam","Akhi","Raw"]

myvar = pd.Series(a)

print(myvar)
'''

a = ("Sam", "Akhi", "Raw")

myvar = pd.Series(a)

print(myvar)

