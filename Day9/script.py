# Day 9: Python Sets

# --------------------------------------------------------
# Task 1: Creating and Accessing Sets
# --------------------------------------------------------

print('...................................Creating and Accessing Sets...................................')

# Creating a set
fruits = {"apple", "banana", "cherry", "apple"}  # Duplicate 'apple' will be removed
print(f"Fruits Set: {fruits}")

# Checking if an element exists in a set
print(f"Is 'banana' in fruits? {'banana' in fruits}")
print(f"Is 'orange' in fruits? {'orange' in fruits}")

# --------------------------------------------------------
# Task 2: Adding and Removing Elements
# --------------------------------------------------------

print('...................................Adding and Removing Elements...................................')

# Adding elements to a set
fruits.add("orange")
print(f"Set after adding 'orange': {fruits}")

# Removing elements from a set
fruits.discard("banana")  # Removes 'banana' if it exists
print(f"Set after removing 'banana': {fruits}")

# --------------------------------------------------------
# Task 3: Set Operations (Union, Intersection, Difference)
# --------------------------------------------------------

print('...................................Set Operations...................................')

# Defining another set
tropical = {"banana", "pineapple", "mango"}

# Union
union_set = fruits.union(tropical)
print(f"Union of Fruits and Tropical: {union_set}")

# Intersection
intersection_set = fruits.intersection(tropical)
print(f"Intersection of Fruits and Tropical: {intersection_set}")

# Difference
difference_set = fruits.difference(tropical)
print(f"Difference of Fruits and Tropical: {difference_set}")

# --------------------------------------------------------
# Task 4: Iterating Over a Set
# --------------------------------------------------------

print('...................................Iterating Over a Set...................................')

# Looping through a set
for fruit in fruits:
    print(fruit)

# --------------------------------------------------------
# Task 5: Practical Use Case
# --------------------------------------------------------

print('...................................Practical Use Case...................................')

# Removing duplicates from a list using a set
numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = set(numbers)
print(f"Unique Numbers: {unique_numbers}")

# Converting back to a list
unique_numbers_list = list(unique_numbers)
print(f"Unique Numbers as List: {unique_numbers_list}")

print('...................................Practical Use Case...................................')
