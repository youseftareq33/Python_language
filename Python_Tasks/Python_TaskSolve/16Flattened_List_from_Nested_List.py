def flatten_list(nested_list):
    flat_list = []
    for sublist in nested_list:
        if isinstance(sublist, list):
            flat_list.extend(flatten_list(sublist))
        else:
            flat_list.append(sublist)
    return flat_list

nested_list = [1, [2, 3, [4, 5]], 6, [7, 8]]
flat_list = flatten_list(nested_list)

print("Flattened list:", flat_list)
