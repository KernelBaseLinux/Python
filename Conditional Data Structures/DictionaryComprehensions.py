'''square_dict = {}
print(type(square_dict))
for key in range(1, 11):
    value = key
    square_dict[key] = value*value
print(square_dict)'''

# dictionary comprehension example
square_dict = {num: num*num for num in range(1, 11)}
print(square_dict)
#item price in dollars

#old_price = {'milk': 1.02, 'coffee': 2.5, 'bread': 2.5}

#dollar_to_pound = 0.76
#new_price = {item: value*dollar_to_pound for (item, value) in old_price.items()}
#print(new_price)

'''new_price = {}
for (item, value) in old_price.items():
    new_price[item] = value*dollar_to_pound

print(new_price)'''
    
