# Here all the iterables are True so all 
# will return True and the same will be printed 
#print (all([True, True, False, True])) 
  
# Here the method will short-circuit at the  
# first item (False) and will return False. 
#print (all([False, True, True, False])) 
  
# This statement will return False, as no 
# True is found in the iterables 
#print (all([False, False, False])) 

# Take two lists  
list1=[] 
list2=[] 
  
# All numbers in list1 are in form: 4*i-3 
for i  in range(1,21): 
    list1.append(4*i-3) 
  
# list2 stores info of odd numbers in list1 
for i in range(0,20): 
    list2.append(list1[i]%2==1) 
  
print('See whether all numbers in list1 are odd =>') 
print(all(list2))
