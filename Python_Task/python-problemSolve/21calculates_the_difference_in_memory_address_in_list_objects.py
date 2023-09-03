def memory_difference(list1, list2):
    address1 = id(list1)
    address2 = id(list2)
    return abs(address1 - address2)

list1 = [1, 2, 3]
list2 = [4, 5, 6]

difference = memory_difference(list1, list2)
print("Memory address difference:", difference)
