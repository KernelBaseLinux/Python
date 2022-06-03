class Person:
  def __init__(self,name, age):
    self.name = name
    self.age = age

  def MyFunc(self):
      print(self.name + self.age)

p1 = Person(4, 36) # instance creation

print(p1.MyFunc())
