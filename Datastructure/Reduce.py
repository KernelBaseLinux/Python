'''
reduce(function, iterables)
'''
from functools import reduce
def add(a,b):
    c = a+b
    return c

print(reduce(add, [23,21,45,98,7,99,9.8,9999]))
#print(reduce(lambda a,b: a+b,[23,21,45,98,7,99,9.8,9999]))
#z = map(lambda x: x*12,[20])
#print(list(z))
