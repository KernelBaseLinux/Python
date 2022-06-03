def ReadFile(arg):
    #a =[]
    file = open(arg, "r")  
    a = file.read()
    return a

def WriteFile(arg):
      file = open(arg, "w")  
      file.write("Hi Alll**")
      file.close()

def ReadWrite(arg):
       file = open(arg, "r+")  
      file.write("Hi Alll**")
