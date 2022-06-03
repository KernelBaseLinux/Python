'''
SYNTAX:
------
map(function, iterables) 
'''
def newfunc(a):
    return a*a

x = map(newfunc, [1,2,3,4])  #x is the map object
print(list(x))

'''
def newfunc(a):
    return a*a
x = map(newfunc, (1,2,3,4))  #x is the map object
print(x)
print(list(x))'''

#tup= (5, 7, 22, 97, 54, 62, 77, 23, 73, 61)
#newtuple = tuple(map(lambda x: x*x , tup)) 
#print(newtuple)
