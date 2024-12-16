# --------------------------------------------------------
# Day 6: Python Lists and Their Operations
# --------------------------------------------------------

# --------------------------------------------------------
# Task 1: Creating and Accessing Lists
# --------------------------------------------------------

print('..............................Creating and Accessing Lists..............................')
print(' ')

# Creating a list
fruits = ["apple", "banana", "cherry", "date", "elderberry"]

# Accessing elements
print(f"First fruit: {fruits[0]}")
print(f"Last fruit: {fruits[-1]}")

# Slicing the list
print(f"First three fruits: {fruits[:3]}")
print(f"Fruits from the second to the last: {fruits[1:]}")

print(' ')
print('..............................Creating and Accessing Lists..............................')
print(' ')

# --------------------------------------------------------
# Task 2: Modifying Lists
# --------------------------------------------------------

print('..............................Modifying Lists..............................')
print(' ')

# Adding elements
fruits.append("fig")
print(f"List after appending 'fig': {fruits}")

# Inserting elements
fruits.insert(2, "grape")
print(f"List after inserting 'grape' at position 2: {fruits}")

# Removing elements
fruits.remove("banana")
print(f"List after removing 'banana': {fruits}")

# Replacing elements
fruits[1] = "blueberry"
print(f"List after replacing the second element with 'blueberry': {fruits}")

print(' ')
print('..............................Modifying Lists..............................')
print(' ')

# --------------------------------------------------------
# Task 3: List Methods
# --------------------------------------------------------

print('..............................List Methods..............................')
print(' ')

# Sorting a list
fruits.sort()
print(f"Sorted list: {fruits}")

# Reversing a list
fruits.reverse()
print(f"Reversed list: {fruits}")

# Counting occurrences
print(f"Number of times 'apple' appears: {fruits.count('apple')}")

# Clearing a list
fruits.clear()
print(f"List after clearing: {fruits}")

print(' ')
print('..............................List Methods..............................')
print(' ')

# --------------------------------------------------------
# Task 4: List Comprehension
# --------------------------------------------------------

print('..............................List Comprehension..............................')
print(' ')

# Creating a list of squares of numbers from 1 to 10
squares = [x**2 for x in range(1, 11)]
print(f"Squares of numbers from 1 to 10: {squares}")

# Creating a list of even numbers from 1 to 20
evens = [x for x in range(1, 21) if x % 2 == 0]
print(f"Even numbers from 1 to 20: {evens}")

print(' ')
print('..............................List Comprehension..............................')
print(' ')

# --------------------------------------------------------
# Task 5: Merging and Copying Lists
# --------------------------------------------------------

print('..............................Merging and Copying Lists..............................')
print(' ')

# Creating two lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]

# Merging lists
merged_list = list1 + list2
print(f"Merged list: {merged_list}")

# Copying a list
copied_list = list1.copy()
print(f"Copied list: {copied_list}")

print(' ')
print('..............................Merging and Copying Lists..............................')
print(' ')
