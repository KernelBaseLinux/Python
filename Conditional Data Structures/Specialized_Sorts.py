#https://docs.python.org/3/howto/sorting.html
#Syntax : sorted(iterable, key, reverse)

# List 
x = [11,3,44,6,7] 
print (sorted(x,reverse=True)) 
  
# Tuple 
x = ('q', 'w', 'e', 'r', 't', 'y') 
print (sorted(x)) 
  
# String-sorted based on ASCII translations 
x = "python"
print (sorted(x)) 
  
# Dictionary 
x = {'q':1, 'w':2, 'e':3, 'r':4, 't':5, 'y':6} 
print (sorted(x)) 
  
# Set 
x = {'q', 'w', 'e', 'r', 't', 'y'} 
print (sorted(x)) 
