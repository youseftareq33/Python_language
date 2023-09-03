'''
Tuples are similar to lists but have some key differences:
1) they cannot be modified after creation
2) and they use parentheses () instead of square brackets [] for defining elements. 

When to Use Tuples:
Tuples are useful when you want to group related data together, especially when the data should not be modified.
They are also used for multiple return values from functions.

Keep in mind that because tuples are immutable, you can't modify,
add, or remove elements after creation. Use lists when you need to modify the contents of the collection.
'''

# Creating Tuples:
my_tuple = (1, 2, 3)
another_tuple = tuple([4, 5, 6])

# Accessing Elements:
my_tuple = (10, 20, 30)
print(my_tuple[0])  # Output: 10
print(my_tuple[1])  # Output: 20

# Tuple Packing and Unpacking:
point = 3, 4
x, y = point
print(x, y)  # Output: 3 4

# Tuple Built-in Methods:

# Tuples are immutable, so they have fewer built-in methods compared to lists.

# tuple methods:

# count(item): Returns the number of occurrences of a specified item in the tuple.
my_tuple = (1, 2, 2, 3, 2)
count = my_tuple.count(2)
print(count)  # Output: 3

# index(item, start, end): Returns the index of the first occurrence of an item within a specified range.
my_tuple = (10, 20, 30, 20)
index = my_tuple.index(20)
print(index)  # Output: 1
