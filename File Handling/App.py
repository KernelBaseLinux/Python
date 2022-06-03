# Python code to create a file
a=[]
file = open('sample.txt','r+')
a = file.readlines()
print(a)
file.close()
