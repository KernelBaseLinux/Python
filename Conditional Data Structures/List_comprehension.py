'''
Syntax
******
newlist = [expression for item in iterable if condition == True]
'''
'''payload_data = []
LFruits = ["apple", "banana", "cherry", "kiwi", "mango"]
payload_data.append(LFruits)
oFruits = ["apple", "banana", "cherry", "kiwi", "mango", "a2"]
payload_data.append(oFruits)
iFruits = ["apple", "banana", "cherry", "kiwi", "mango", "a3"]
payload_data.append(iFruits)


#function defination
def new_list(data1, data2):
    newlist = []
    for x in data1, data2:
        #print(type(x))
        print(x)
        for i in x:
          #print("my i value is: ", i)
          if "a" in i:
            #print(i)
            newlist.append(i)
    print("My List:        ", newlist)

#for i in payload_data:
#    new_list(i) 
new_list(LFruits, oFruits) # function call
#new_list(oFruits)
#new_list(iFruits)
#new_list(jFruits)
'''
#Number = [1,2,3,4,5,6,7,8,9,10,11,12] # or range(0-100) find the even number
#fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
#newlist = [x for x in fruits if "a" in x]
EvenList = [x for x in range(0,100) if x%2 == 0]
print(EvenList)

#newlist = [x for x in fruits if x != "apple"]'''



