import json
#json.load() method to read a file containing JSON object.
with open('Sample.json') as f:
  data = json.load(f)
print(type(data))
