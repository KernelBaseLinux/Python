'''
Python supports a dictionary like a container called UserDict present
in the collections module. This class acts as a wrapper class around
the dictionary objects. This class is useful when one wants to create a
dictionary of their own with some modified functionality or with some new
functionality. It can be considered as a way of adding new behaviors for
the dictionary. This class takes a dictionary instance as an argument and
simulates a dictionary that is kept in a regular dictionary.
The dictionary is accessible by the data attribute of this class.
'''
from collections import UserDict
  
  
d = {'a':1,
    'b': 2,
    'c': 3}
b = {'f':1,
    'g': 2,
    'h': 3}
print(type(d))
# Creating an UserDict
userD = UserDict(d)
userD = UserDict(b)
print(type(userD))
print(userD.data)
  
  
# Creating an empty UserDict
userD = UserDict()
print(userD)
