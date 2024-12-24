# Day 15: Python Sets

# --------------------------------------------------------
# Task 1: Creating and Accessing Sets
# --------------------------------------------------------

print('...................................Creating and Accessing Sets...................................')

# Creating sets
fruits = {"apple", "banana", "cherry"}
numbers = {1, 2, 3, 4, 5}

# Displaying sets
print(f"Fruits Set: {fruits}")
print(f"Numbers Set: {numbers}")

# Checking membership
print(f"Is 'apple' in the fruits set? {'apple' in fruits}")
print(f"Is 6 in the numbers set? {6 in numbers}")

# --------------------------------------------------------
# Task 2: Adding and Removing Elements
# --------------------------------------------------------

print('...................................Adding and Removing Elements...................................')

# Adding elements
fruits.add("orange")
print(f"Fruits Set after adding 'orange': {fruits}")

# Removing elements
fruits.discard("banana")
print(f"Fruits Set after removing 'banana': {fruits}")

# --------------------------------------------------------
# Task 3: Set Operations
# --------------------------------------------------------

print('...................................Set Operations...................................')

# Creating two sets
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# Union
print(f"Union of A and B: {A | B}")

# Intersection
print(f"Intersection of A and B: {A & B}")

# Difference
print(f"Difference of A and B: {A - B}")

# Symmetric Difference
print(f"Symmetric Difference of A and B: {A ^ B}")

# --------------------------------------------------------
# Task 4: Practical Use Case
# --------------------------------------------------------

print('...................................Practical Use Case...................................')

# Removing duplicates from a list using sets
numbers_with_duplicates = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = set(numbers_with_duplicates)

print(f"Original List with Duplicates: {numbers_with_duplicates}")
print(f"Unique Numbers (Duplicates Removed): {unique_numbers}")

print('...................................Practical Use Case...................................')