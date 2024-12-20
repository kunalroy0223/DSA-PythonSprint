# Day 11: Python Sets

# --------------------------------------------------------
# Task 1: Creating and Using Sets
# --------------------------------------------------------

print('...................................Creating and Using Sets...................................')

# Creating a set
fruits = {"apple", "banana", "cherry", "apple"}  # Duplicate elements are ignored
print(f"Fruits Set: {fruits}")

# Checking membership
print(f"Is 'apple' in fruits? {'apple' in fruits}")
print(f"Is 'mango' in fruits? {'mango' in fruits}")

# Adding elements
fruits.add("mango")
print(f"Set after adding 'mango': {fruits}")

# Removing elements
fruits.remove("banana")  # Raises KeyError if element is not found
print(f"Set after removing 'banana': {fruits}")

# Using discard (does not raise an error if the element is not found)
fruits.discard("grape")
print(f"Set after discarding 'grape': {fruits}")

# --------------------------------------------------------
# Task 2: Set Operations
# --------------------------------------------------------

print('...................................Set Operations...................................')

# Creating two sets
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# Union
union_set = A.union(B)
print(f"Union of A and B: {union_set}")

# Intersection
intersection_set = A.intersection(B)
print(f"Intersection of A and B: {intersection_set}")

# Difference
difference_set = A.difference(B)
print(f"Difference (A - B): {difference_set}")

# Symmetric Difference
symmetric_difference_set = A.symmetric_difference(B)
print(f"Symmetric Difference of A and B: {symmetric_difference_set}")

# --------------------------------------------------------
# Task 3: Practical Use Case
# --------------------------------------------------------

print('...................................Practical Use Case...................................')

# Removing duplicates from a list using a set
numbers = [1, 2, 3, 2, 1, 4, 5, 4, 6]
unique_numbers = list(set(numbers))
print(f"Original List: {numbers}")
print(f"Unique Numbers: {unique_numbers}")

print('...................................Practical Use Case...................................')
