class MyClass():
    def __init__(self,a,b): #construtor
        self.a = a
        self.b = b
        print("I am in constructor!!!!!")
        
    def add(self):
        d = self.a + self.b
        return d

Obj = MyClass(1,2)
print(Obj.add())
