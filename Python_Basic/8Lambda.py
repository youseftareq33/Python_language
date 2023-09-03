'''
 lambda functions when the function logic is simple and can be expressed in a single expression.
   For more complex functions, it's better to use named functions.

They can only contain a single expression, not multiple statements.
They cannot have documentation strings (docstrings).
They are less readable than named functions for complex operations.

'''

# Creating a lambda function that adds two numbers.
add = lambda x, y: x + y
result = add(3, 5)
print(result)  # Output: 8

# its often use in:

# Using Lambda with map():
numbers = [1, 2, 3, 4, 5]
squared = map(lambda x: x ** 2, numbers)
print(list(squared))  # Output: [1, 4, 9, 16, 25]

# Using Lambda with filter():
numbers = [1, 2, 3, 4, 5, 6]
evens = filter(lambda x: x % 2 == 0, numbers)
print(list(evens))  # Output: [2, 4, 6]

# Using Lambda with sorted():
words = ["apple", "banana", "cherry", "date"]
sorted_words = sorted(words, key=lambda x: len(x))
print(sorted_words)  # Output: ['date', 'apple', 'cherry', 'banana']
