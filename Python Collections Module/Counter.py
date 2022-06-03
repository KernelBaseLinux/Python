#Syntax:- class collections.Counter([iterable-or-mapping])
'''
Initializing Counter Objects
The counter object can be initialized using the counter()
function and this function can be called in one of the following ways:

With a sequence of items
With a dictionary containing keys and counts
With keyword arguments mapping string names to counts

for more Info:- https://www.geeksforgeeks.org/counters-in-python-set-1/
*************************************************************************
A counter is a sub-class of the dictionary. It is used to keep the count
of the elements in an iterable in the form of an unordered dictionary
where the key represents the element in the
iterable and value represents the count of that element in the iterable.
*************************************************************************
'''
# A Python program to show different  
# ways to create Counter  
from collections import Counter  
    
# With sequence of items   
print(Counter(['B','B','A','B','C','A','B', 
               'B','A','C'])) 
    
# with dictionary  
print(Counter({'A':3, 'B':5, 'C':2})) 
    
# with keyword arguments  
print(Counter(A=3, B=5, C=2))
