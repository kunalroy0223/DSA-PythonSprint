# --------------------------------------------------------
# Day 5: Strings and Their Operations in Python
# --------------------------------------------------------

# --------------------------------------------------------
# Task 1: Basic String Operations
# --------------------------------------------------------

print('..............................Basic String Operations..............................')
print(' ')

# Defining a string
greeting = "Hello, Python Learners!"

# Printing the original string
print(f"Original String: {greeting}")

# String length
print(f"Length of the string: {len(greeting)}")

# Accessing characters
print(f"First character: {greeting[0]}")
print(f"Last character: {greeting[-1]}")

# String slicing
print(f"Substring (0-5): {greeting[0:5]}")
print(f"Substring (7 onwards): {greeting[7:]}")

print(' ')
print('..............................Basic String Operations..............................')
print(' ')

# --------------------------------------------------------
# Task 2: String Methods
# --------------------------------------------------------

print('..............................String Methods..............................')
print(' ')

# Converting to uppercase and lowercase
print(f"Uppercase: {greeting.upper()}")
print(f"Lowercase: {greeting.lower()}")

# Checking for substrings
print(f"Does the string contain 'Python'? {'Python' in greeting}")

# Replacing substrings
replaced_string = greeting.replace("Python Learners", "World")
print(f"Replaced String: {replaced_string}")

print(' ')
print('..............................String Methods..............................')
print(' ')

# --------------------------------------------------------
# Task 3: String Formatting
# --------------------------------------------------------

print('..............................String Formatting..............................')
print(' ')

# Defining variables
name = "Alice"
age = 25
language = "Python"

# Using f-strings for formatting
print(f"My name is {name}. I am {age} years old, and I love learning {language}!")

# Using the format method
print("My name is {}. I am {} years old, and I love learning {}!".format(name, age, language))

# Aligning text
print(f"Right aligned: {'Python':>10}")
print(f"Left aligned: {'Python':<10}")

print(' ')
print('..............................String Formatting..............................')
print(' ')

# --------------------------------------------------------
# Task 4: Palindrome Checker
# --------------------------------------------------------

print('..............................Palindrome Checker..............................')
print(' ')

# Input a string to check for palindrome
input_string = input("Enter a string to check if it's a palindrome: ").lower().replace(" ", "")

# Checking if the string is a palindrome
if input_string == input_string[::-1]:
    print(f"The string '{input_string}' is a palindrome!")
else:
    print(f"The string '{input_string}' is not a palindrome.")

print(' ')
print('..............................Palindrome Checker..............................')
print(' ')
