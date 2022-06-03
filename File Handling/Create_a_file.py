# Python code to create a file
a=[]
file = open('43425555543.txt','r+') 
file.write("\n*********This is the write command########") 
a = file.read()
print(type(a))
file.close() 
