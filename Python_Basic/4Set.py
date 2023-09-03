# Creating a Set:
unique_numbers = {1, 2, 3, 4, 5}

# Checking membership
if 3 in unique_numbers:
    print("3 is in the set")

# Adding a single element
unique_numbers.add(6)

# Adding multiple elements
unique_numbers.update([7, 8, 9])

# Removing an element
unique_numbers.remove(4)  # Raises an error if the element doesn't exist

# Removing an element safely
unique_numbers.discard(10)  # No error even if the element doesn't exist

# Clearing all elements in the set
unique_numbers.clear()

#len(): Returns the number of elements in the set.
num_elements = len(unique_numbers)
print("Number of elements:", num_elements)

#pop(): Removes and returns an arbitrary element from the set.
popped_element = unique_numbers.pop()  # Raises an error if the set is empty
print("Popped element:", popped_element)

#issubset() and issuperset(): Check if a set is a subset or superset of another set.
set_a = {1, 2, 3}
set_b = {1, 2, 3, 4, 5}

is_subset = set_a.issubset(set_b)
is_superset = set_b.issuperset(set_a)

print("Is A a subset of B?", is_subset)
print("Is B a superset of A?", is_superset)

#Set Operations:
#Union (|): Combines elements from two sets, removing duplicates.
set_a = {1, 2, 3}
set_b = {3, 4, 5}

union_set = set_a | set_b
print("Union:", union_set)

#Intersection (&): Returns elements present in both sets.
intersection_set = set_a & set_b
print("Intersection:", intersection_set)

# Difference (-): Returns elements in the first set but not in the second.
difference_set = set_a - set_b
print("Difference:", difference_set)

#Symmetric Difference (^): Returns elements present in either set, but not in both.
symmetric_difference_set = set_a ^ set_b
print("Symmetric Difference:", symmetric_difference_set)