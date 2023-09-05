# del:
my_list1 = [1, 2, 3, 4, 5]
del my_list1[2]  
print(my_list1)  

#----------------------------------------------------------------
# remove:
my_list2 = [1, 2, 3, 4, 3, 5]
my_list2.remove(3)  
print(my_list2)  

#----------------------------------------------------------------
# pop:
my_list3 = [1, 2, 3, 4, 5]
popped_value = my_list3.pop(2)  
print("Popped value:", popped_value)  
print("Updated list:", my_list3)  

#----------------------------------------------------------------
'''
Use del when you want to remove an element by index and don't need the value.
Use remove() when you want to remove an element by value and don't need the index.
Use pop() when you want to remove an element by index and need the removed value. If no index is provided, it removes the last element.
'''