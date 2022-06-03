#The frozenset() function returns an immutable frozenset object,
#initialized with elements from the given iterable.
#Syntax: - frozenset([iterable])

person = {"name": "John", "age": 23, "sex": "male"}
fSet = frozenset(person)
print('The frozen set is:', fSet)
