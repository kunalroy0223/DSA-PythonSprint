import math

# --------------------------------------------------------
# Day 2: Python Basics - Conditional Statements, Loops, and Lists
# --------------------------------------------------------

# --------------------------------------------------------
# Task 1: Understanding Conditional Statements
# --------------------------------------------------------

print('...................................Conditional Statements...................................')

# Take user input and categorize age
age = int(input("Enter your age: "))

if age < 18:
    print("You are a minor.")
elif 18 <= age <= 65:
    print("You are an adult.")
else:
    print("You are a senior citizen.")

print('...................................Conditional Statements...................................')
print()

# --------------------------------------------------------
# Task 2: Loops in Action
# --------------------------------------------------------

print('...................................Loops...................................')

# Using a for loop to print numbers from 1 to 10
print("For loop - Counting from 1 to 10:")
for i in range(1, 11):
    print(i)

# --------------------------------------------------------
# Task 3: Loops - Factorial of a Number
# --------------------------------------------------------

print('..............................Factorial of a Number..............................')
print(' ')

# Taking user input for the number
num = int(input("Enter a number to calculate its factorial: "))

# Initializing the factorial variable
factorial = 1

# Calculating factorial using a for loop
if num < 0:
    print("Factorial is not defined for negative numbers.")
elif num == 0:
    print("The factorial of 0 is 1.")
else:
    for i in range(1, num + 1):
        factorial *= i
    print(f"The factorial of {num} is: {factorial}")

print(' ')
print('..............................Factorial of a Number..............................')
print(' ')


print('...................................Loops...................................')
print()

# --------------------------------------------------------
# Task 3: Lists and Basic Operations
# --------------------------------------------------------

print('...................................Lists and Operations...................................')

# Create a list of fruits
fruits = ["apple", "banana", "cherry", "date"]

# Print the list
print(f"Original list: {fruits}")

# Append a fruit
fruits.append("elderberry")
print(f"After appending: {fruits}")

# Remove a fruit
fruits.remove("banana")
print(f"After removing banana: {fruits}")

# Sort the list
fruits.sort()
print(f"After sorting: {fruits}")

# Access elements using indexing
print(f"First fruit: {fruits[0]}")
print(f"Last fruit: {fruits[-1]}")

print('...................................Lists and Operations...................................')
print()
