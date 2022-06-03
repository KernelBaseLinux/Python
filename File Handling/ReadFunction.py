'''
read() would treat each character in the file separately,
meaning that the iteration would happen for every character. The readline()
function, on the other hand, only reads a single line of the file
'''
data = []
file = open("5000 BT Records.csv")   
data = file.readlines()

for i in data:
    print(i)
