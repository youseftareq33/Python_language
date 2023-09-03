# Using in with Dictionary
student_grades = {"ahmad": 85, "rami": 92, "diaa": 78}
name_to_check = "rami"

if name_to_check in student_grades:
    print("exists")
else:
    print("not exists")

# Using in with List
fruits = ["apple", "banana", "orange", "grape"]
fruit_to_check = "orange"

if fruit_to_check in fruits:
    print("exists")
else:
    print("not exists")

# Using in with Tuple
days_of_week = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")
day_to_check = "Sunday"

if day_to_check in days_of_week:
    print("exists")
else:
    print("not exists")
