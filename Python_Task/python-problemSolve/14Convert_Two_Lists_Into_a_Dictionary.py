def lists_to_dictionary(keys, values):
    dictionary = {keys[i]: values[i] for i in range(len(keys))}
    return dictionary

keys = ['name', 'age', 'city']
values = ['Ayman', 25, 'Nablus']

result_dict = lists_to_dictionary(keys, values)
print("Resulting dictionary:", result_dict)
