import copy
old_list = [1,2,3,4,5,6]
new_list = old_list

new_list[2] = 9

print('Old List:', old_list)
print('ID of Old List:', id(old_list))

print('New List:', new_list)
print('ID of New List:', id(new_list))
