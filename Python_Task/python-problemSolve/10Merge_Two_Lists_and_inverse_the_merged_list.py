def merge_and_inverse(list1, list2):
    merged_list = list1 + list2
    inverse_list = merged_list[::-1]
    return inverse_list

list1 = [1, 2, 3]
list2 = [4, 5, 6]

merged_and_inversed = merge_and_inverse(list1, list2)

print("Merged and Inversed List:", merged_and_inversed)
