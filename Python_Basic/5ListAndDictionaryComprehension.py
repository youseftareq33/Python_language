# List Comprehension:


# new_list = [expression for item in sequence if condition]

# Creating a list of squares of even numbers from 0 to 9.
squares_of_evens = [x**2 for x in range(10) if x % 2 == 0]
print(squares_of_evens)  # Output: [0, 4, 16, 36, 64]

#-----------------------------------------------------------
# Dictionary Comprehension:

#new_dict = {key_expression: value_expression for item in sequence if condition}

# Creating a dictionary of squares of numbers from 0 to 4 as keys and their cubes as values.
squares_and_cubes = {x: x**3 for x in range(5)}
print(squares_and_cubes)  # Output: {0: 0, 1: 1, 2: 8, 3: 27, 4: 64}

# You can also use dictionary comprehension to transform an existing dictionary by applying an expression to its keys or values.
original_dict = {'a': 1, 'b': 2, 'c': 3}
transformed_dict = {key: value * 2 for key, value in original_dict.items()}
print(transformed_dict)  # Output: {'a': 2, 'b': 4, 'c': 6}
