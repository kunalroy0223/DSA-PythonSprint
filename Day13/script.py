# Day 13: Python Sets

# --------------------------------------------------------
# Task 1: Creating and Accessing Sets
# --------------------------------------------------------

print('...................................Creating and Accessing Sets...................................')

# Creating sets
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

# Displaying sets
print(f"Set A: {set_a}")
print(f"Set B: {set_b}")

# Adding elements to a set
set_a.add(6)
print(f"Set A after adding 6: {set_a}")

# Removing elements from a set
set_a.discard(2)
print(f"Set A after discarding 2: {set_a}")

# --------------------------------------------------------
# Task 2: Set Operations
# --------------------------------------------------------

print('...................................Set Operations...................................')

# Union of sets
union_set = set_a.union(set_b)
print(f"Union of Set A and Set B: {union_set}")

# Intersection of sets
intersection_set = set_a.intersection(set_b)
print(f"Intersection of Set A and Set B: {intersection_set}")

# Difference of sets
difference_set = set_a.difference(set_b)
print(f"Difference of Set A and Set B: {difference_set}")

# Symmetric Difference of sets
symmetric_difference_set = set_a.symmetric_difference(set_b)
print(f"Symmetric Difference of Set A and Set B: {symmetric_difference_set}")

# --------------------------------------------------------
# Task 3: Checking Membership
# --------------------------------------------------------

print('...................................Checking Membership...................................')

# Membership testing
print(f"Is 3 in Set A? {'Yes' if 3 in set_a else 'No'}")
print(f"Is 10 in Set B? {'Yes' if 10 in set_b else 'No'}")

# --------------------------------------------------------
# Task 4: Practical Use Case
# --------------------------------------------------------

print('...................................Practical Use Case...................................')

# Removing duplicates from a list using a set
numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = list(set(numbers))
print(f"Original List: {numbers}")
print(f"List after removing duplicates: {unique_numbers}")

print('...................................Practical Use Case...................................')
