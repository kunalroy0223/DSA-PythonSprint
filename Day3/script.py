# --------------------------------------------------------
# Day 3: Control Statements and String Manipulations
# --------------------------------------------------------

# --------------------------------------------------------
# Task 1: Control Statements - Checking Odd or Even
# --------------------------------------------------------

print('..............................Checking Odd or Even..............................')
print(' ')

# Taking user input
number = int(input("Enter a number: "))

# Using if-else to check if the number is odd or even
if number % 2 == 0:
    print(f"{number} is an even number.")
else:
    print(f"{number} is an odd number.")

print(' ')
print('..............................Checking Odd or Even..............................')
print(' ')

# --------------------------------------------------------
# Task 2: Nested If - Checking Leap Year
# --------------------------------------------------------

print('..............................Checking Leap Year..............................')
print(' ')

# Taking user input for the year
year = int(input("Enter a year to check if it's a leap year: "))

# Nested if conditions for leap year
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is a leap year.")
        else:
            print(f"{year} is not a leap year.")
    else:
        print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

print(' ')
print('..............................Checking Leap Year..............................')
print(' ')

# --------------------------------------------------------
# Task 3: String Manipulations - Reversing a String
# --------------------------------------------------------

print('..............................Reversing a String..............................')
print(' ')

# Taking input for a string
user_string = input("Enter a string to reverse: ")

# Reversing the string using slicing
reversed_string = user_string[::-1]

# Displaying the reversed string
print(f"The reversed string is: {reversed_string}")

print(' ')
print('..............................Reversing a String..............................')
print(' ')

# --------------------------------------------------------
# Task 4: String Manipulations - Palindrome Check
# --------------------------------------------------------

print('..............................Checking for Palindrome..............................')
print(' ')

# Taking input for a string
palindrome_string = input("Enter a string to check for palindrome: ")

# Checking if the string is the same when reversed
if palindrome_string == palindrome_string[::-1]:
    print(f"The string '{palindrome_string}' is a palindrome.")
else:
    print(f"The string '{palindrome_string}' is not a palindrome.")

print(' ')
print('..............................Checking for Palindrome..............................')
print(' ')
