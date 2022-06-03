'''
File Handling mode
******************
“ r “, for reading.
“ w “, for writing.
“ a “, for appending.
“ r+ “, for both reading and writing

file = open('sample.txt', 'r')  
for each in file: 
    print (each) 
file.close()
'''
#file = open("sample.txt", "r")  
#print (file.readlines())

# Python code to illustrate read() mode character wise

a =[]
b = []
count =0
data = ""
file = open("sample.txt", "r") 
a= file.readlines()
for i in a:
    count += 1
    if "differently" in i:
        #print(count)
        b = i.split(" ")
        #print(b)
       
        for i in b[::-1]:
            #print(i)
            if "\n" in i:
                i = i.strip("\n")
                data +=" "+ i
            else:
                data +=" "+ i
print(data)
        
        
        

