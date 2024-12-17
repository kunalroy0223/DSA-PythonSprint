# Day 7: Tuples and Sets in Python

# --------------------------------------------------------
# Task 1: Working with Tuples
# --------------------------------------------------------

print('...................................Working with Tuples...................................')

# Creating a tuple
my_tuple = (1, 2, 3, 4, 5)

# Accessing elements using indexing
print(f"Element at index 2: {my_tuple[2]}")

# Slicing a tuple
print(f"Sliced tuple (from index 1 to 4): {my_tuple[1:4]}")

# Tuple with single element
single_element_tuple = (10,)
print(f"Single element tuple: {single_element_tuple}")

# --------------------------------------------------------
# Task 2: Working with Sets
# --------------------------------------------------------

print('...................................Working with Sets...................................')

# Creating a set
my_set = {1, 2, 3, 4, 5}

# Adding elements to a set
my_set.add(6)
print(f"Set after adding an element: {my_set}")

# Removing elements from a set
my_set.remove(3)
print(f"Set after removing an element: {my_set}")

# Performing set operations
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Union of sets
union_set = set1.union(set2)
print(f"Union of sets: {union_set}")

# Intersection of sets
intersection_set = set1.intersection(set2)
print(f"Intersection of sets: {intersection_set}")

# Difference of sets
difference_set = set1.difference(set2)
print(f"Difference of sets: {difference_set}")

# --------------------------------------------------------
# Task 3: Nested Tuples and Sets
# --------------------------------------------------------

print('...................................Nested Tuples and Sets...................................')

# Nested tuple
nested_tuple = ((1, 2), (3, 4), (5, 6))
print(f"Nested tuple: {nested_tuple}")

# Nested set
nested_set = {frozenset([1, 2]), frozenset([3, 4])}
print(f"Nested set: {nested_set}")

# --------------------------------------------------------
# Task 4: Applications of Tuples and Sets
# --------------------------------------------------------

print('...................................Applications of Tuples and Sets...................................')

# Using tuple to store data (immutable, used for coordinates, etc.)
coordinates = (10.5, 20.3)
print(f"Coordinates (tuple): {coordinates}")

# Using set for fast membership testing
check_set = {1, 2, 3, 4, 5}
element = 3
if element in check_set:
    print(f"Element {element} is present in the set.")

print('...................................Applications of Tuples and Sets...................................')
