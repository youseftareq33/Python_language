def delete_element(dictionary, key):
    if key in dictionary:
        del dictionary[key]
        return True
    else:
        return False

my_dict = {'a': 1, 'b': 2, 'c': 3}

key_to_delete = 'b'
deleted = delete_element(my_dict, key_to_delete)

if deleted:
    print("Key ",key_to_delete," deleted\n"+"Updated dictionary:", my_dict)
else:
    print("key not found")
