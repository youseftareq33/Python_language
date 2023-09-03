# Creating a dictionary
student_scores = {
    "Alice": 95,
    "Bob": 78,
    "Charlie": 85,
    "David": 92,
    "Emily": 88
}

# Accessing values using keys
alice_score = student_scores["Alice"]
print("Alice's score:", alice_score)

# Adding a new key-value pair
student_scores["Frank"] = 70

# Modifying an existing value
student_scores["Bob"] = 82

# Removing a key-value pair
del student_scores["Charlie"]

# len(): Returns the number of key-value pairs in the dictionary.
num_students = len(student_scores)
print("Number of students:", num_students)

# keys(): Returns a view of all keys in the dictionary.
all_names = student_scores.keys()
print("All names:", all_names)

# values(): Returns a view of all values in the dictionary.
all_scores = student_scores.values()
print("All scores:", all_scores)

# items(): Returns a view of all key-value pairs in the dictionary as tuples.
all_entries = student_scores.items()
print("All entries:", all_entries)

# Iterating through a Dictionary:
# You can use loops to iterate through dictionaries.

# Iterating through keys
for name in student_scores:
    print(name, ":", student_scores[name])

# Or using the .items() method to iterate through key-value pairs:

# Iterating through key-value pairs
for name, score in student_scores.items():
    print(name, ":", score)

# Safely Accessing Values:
# The get() method allows you to access values safely, providing a default value if the key doesn't exist.
grace_score = student_scores.get("Grace", "Score not found")
print("Grace's score:", grace_score)

# Removing with Pop():
#The pop() method removes a key and returns its corresponding value.
emily_score = student_scores.pop("Emily")
print("Emily's score:", emily_score)