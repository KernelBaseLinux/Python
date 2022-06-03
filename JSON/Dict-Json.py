#Convert dict to JSON[convert a dictionary to JSON string using json.dumps() method.]
from json import *

person_dict = {'valume': 67,'age': 12,'children': None}
print(type(person_dict))
person_json = dumps(person_dict)
print(type(person_json))
