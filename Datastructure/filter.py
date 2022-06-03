'''
filter(function, iterables)
'''

'''def func(x):
    if x%2==0:
        return x
    
y = filter(func,range(0,50))  #call
print(type(y))
print(list(y))'''

#print(str(y))

y = filter(lambda x: x%2==0, (1,2,3,4))
print(tuple(y))

