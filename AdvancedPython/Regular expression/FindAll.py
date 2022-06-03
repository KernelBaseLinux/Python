import re

'''string = 'hello 12 hi 8. Howdy 34 6666'
pattern = '^1\d+'


result = re.findall(pattern, string)
if(result):
    print(result)



string = 'Twelve:12 Eighty nine:89.'
pattern = ' '

result = re.split(pattern, string) 
print(result)

# multiline string
string = 'abc 12\ de 23                    f45 6'

# matches all whitespace characters
pattern = '\s+'

# empty string
replace = ''

new_string = re.sub(pattern, replace, string) 
print(new_string)'''


string = "Python is fun Python Python"

# check if 'Python' is at the beginning
match = re.search('Python', string)

if match:
  print(match.group(0))
  
  
else:
  print("pattern not found") 

