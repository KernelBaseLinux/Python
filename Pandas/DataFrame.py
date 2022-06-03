import pandas as pd
'''
pandas.DataFrame( data, index, columns, dtype, copy)
	
1.data
----
data takes various forms like ndarray, series, map, lists, dict, constants and also another DataFrame.

2.index
-----
For the row labels, the Index to be used for the resulting frame is Optional Default np.arange(n) if no index is passed.

3.columns:
--------
For column labels, the optional default syntax is - np.arange(n). This is only true if no index is passed.

4.dtype
--------
Data type of each column.

5.copy
------
This command (or whatever it is) is used for copying of data, if the default is False.
'''
'''
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

#load data into a DataFrame object:
df = pd.DataFrame(data)

print(df) '''

data = [['Alex',10],['Bob',12],['Clarke',13]]
df = pd.DataFrame(data,columns=['Name','Age'])
print(df)
