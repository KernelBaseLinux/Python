import json
#JSON string using json.loads() method. The method returns a dictionary.
person = {"name": 55, "languages": ["English", "Fench"]}
print("type:---> ", type(person))
person_dict = json.loads(person)
print("Type: ", type(person_dict))
#person_dict['name'] = "add"
print( person_dict)
print(person_dict['name'])
