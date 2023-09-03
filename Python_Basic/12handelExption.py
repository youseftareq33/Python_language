# Try-Except Block:
try:
    # Code that may raise an exception
    result = 10 / 0
except ZeroDivisionError:
    # Code to handle the ZeroDivisionError exception
    print("Division by zero is not allowed.")


# Handling Multiple Exceptions:
try:
    x = int(input("Enter a number: "))
    result = 10 / x
except ValueError:
    print("Invalid input. Please enter a number.")
except ZeroDivisionError:
    print("Division by zero is not allowed.")


# Handling All Exceptions:
'''
try:
    # Code that may raise an exception
except Exception as e:
    # Code to handle any exception
    print("An error occurred:", e)

'''


# Finally Block:
'''
try:
    # Code that may raise an exception
except Exception as e:
    # Code to handle the exception
finally:
    # Code that will always execute

'''
