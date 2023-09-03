# Reading from Files:
'''
You can read the contents of a file using the open() function
'''
with open('example.txt', 'r') as file:
    content = file.read()  # Reads the entire content as a single string
    lines = file.readlines()  # Reads lines into a list

print(content)
print(lines)

#----------------------------------------------------------------------------------------------------------
# Writing to Files:
'''
To write to a file, you can use the open() function with the 'w' mode, followed by the write() method.
'''
with open('output.txt', 'w') as file:
    file.write("Hello, world!\n")
    file.write("This is a new line.")

# If you want to append to an existing file instead of overwriting its content, use the 'a' mode.
# Open the file for appending
with open('output.txt', 'a') as file:
    file.write("\nThis line is appended.")

#----------------------------------------------------------------------------------------------------------
# Reading and Writing Binary Files:
'''
For reading and writing binary files, use the 'rb' (read binary) and 'wb' (write binary) modes, respectively.
'''
# Reading a binary file
with open('image.jpg', 'rb') as file:
    binary_data = file.read()

# Writing to a binary file
with open('new_image.jpg', 'wb') as file:
    file.write(binary_data)

#----------------------------------------------------------------------------------------------------------
# Using Context Managers (with Statement):
'''
Using the with statement ensures that files are properly closed after the block of code is executed, even if an exception occurs.
'''
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)
# File is automatically closed outside the 'with' block

#----------------------------------------------------------------------------------------------------------
# Handling Exceptions:
'''
File operations can result in errors, such as when the file doesn't exist. It's important to handle exceptions using try and except blocks.
'''
try:
    with open('nonexistent.txt', 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File not found.")
