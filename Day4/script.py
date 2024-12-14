# --------------------------------------------------------
# Day 4: Loops and Lists in Python
# --------------------------------------------------------

# --------------------------------------------------------
# Task 1: Using For Loop - Printing Multiplication Table
# --------------------------------------------------------

print('..............................Multiplication Table..............................')
print(' ')

# Input a number for which the multiplication table is to be printed
num = int(input("Enter a number to generate its multiplication table: "))

# Generating the multiplication table using a for loop
print(f"Multiplication table for {num}:")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

print(' ')
print('..............................Multiplication Table..............................')
print(' ')

# --------------------------------------------------------
# Task 2: Using While Loop - Sum of Digits
# --------------------------------------------------------

print('..............................Sum of Digits..............................')
print(' ')

# Input a number to calculate the sum of its digits
number = int(input("Enter a number to calculate the sum of its digits: "))
original_number = number
sum_of_digits = 0

# While loop to calculate the sum of digits
while number > 0:
    digit = number % 10
    sum_of_digits += digit
    number //= 10

print(f"The sum of the digits of {original_number} is: {sum_of_digits}")

print(' ')
print('..............................Sum of Digits..............................')
print(' ')

# --------------------------------------------------------
# Task 3: Working with Lists - Basic Operations
# --------------------------------------------------------

print('..............................Working with Lists..............................')
print(' ')

# Creating a list of numbers
numbers = [10, 20, 30, 40, 50]

# Displaying the list
print(f"The original list is: {numbers}")

# Adding an element to the list
numbers.append(60)
print(f"List after adding an element: {numbers}")

# Removing an element from the list
numbers.remove(30)
print(f"List after removing an element: {numbers}")

# Sorting the list
numbers.sort()
print(f"Sorted list: {numbers}")

print(' ')
print('..............................Working with Lists..............................')
print(' ')

# --------------------------------------------------------
# Task 4: Using Loops with Lists - Finding Maximum and Minimum
# --------------------------------------------------------

print('..............................Finding Maximum and Minimum..............................')
print(' ')

# Using a loop to find the maximum and minimum values in a list
list_values = [15, 3, 98, 44, 56, 72, 19]
print(f"List values: {list_values}")

# Finding the maximum and minimum values using loops
max_value = list_values[0]
min_value = list_values[0]

for value in list_values:
    if value > max_value:
        max_value = value
    if value < min_value:
        min_value = value

print(f"The maximum value in the list is: {max_value}")
print(f"The minimum value in the list is: {min_value}")

print(' ')
print('..............................Finding Maximum and Minimum..............................')
print(' ')
