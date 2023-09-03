# Conditional Statements (if, elif, else):

# if elif else 
number = 0

if number > 0:
    print("Positive number")

elif number == 0:
    print('Zero')
else:
    print('Negative number')

print('This statement is always executed')

# Loops (for and while):

# for loops
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    if fruit=="banana":
        break
    else:
        print(fruit)

# while loops
count = 5
while count > 0:
    print(count)
    count -= 1