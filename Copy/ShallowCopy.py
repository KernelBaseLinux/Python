import copy

'''
Case 1
******
in the below program, we created a shallow copy of old_list.
The new_list contains references to original nested objects stored in old_list.
Then we add the new list i.e 100 into old_list. This new sublist was
not copied in new_list.
However, when you change any nested objects in old_list,
the changes appear in new_list.
'''
'''
old_list = [1,2,3,4,5,6]
new_list = copy.copy(old_list)

old_list.append(100)

print("Old list:", old_list)
print("New list:", new_list)'''

'''
Case 2
******
In the above program, we made changes to old_list
i.e old_list[0][0] = 'AA'. Both sublists of old_list and new_list
at index [0][0] were modified. This is because,
both lists share the reference of same nested objects.
'''

import copy

old_list = [[1], 2, [3]]
new_list = copy.copy(old_list)

old_list[2][0] = 'AA'

print("Old list:", old_list)
print("New list:", new_list)
