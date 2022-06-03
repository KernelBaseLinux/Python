'''
map(function, iterable(s))

def sample(a):
    if a == 2:
        return True
    else:
        return False



l = [1,2,2,3,4,2,6]
a = map(sample,l)

print(list(a))
'''

fruit = ["Apple", "Banana", "Pear", "Apricot", "Orange"]
map_object = map(lambda s: s[0] == "A", fruit)

print(list(map_object))
