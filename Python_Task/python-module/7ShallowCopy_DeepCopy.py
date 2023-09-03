import copy

list= [1, [2, 3], 4]
shallow_copy_list= copy.copy(list)
deep_copy_list= copy.deepcopy(list)

print(shallow_copy_list)
print(deep_copy_list)