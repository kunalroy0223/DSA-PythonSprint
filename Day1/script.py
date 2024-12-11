import math

# --------------------------------------------------------
# Task 1: Print "Hello, World!"
# --------------------------------------------------------

print('...................................Printing Hello, World!...................................')
print(' ')
# Printing "Hello, World!" to the screen
print("Hello, Python Learners!")
print(' ')
print('...................................Printing Hello, World!...................................')
print(' ')

# --------------------------------------------------------
# Task 2: Declaring Variables & Data Types
# --------------------------------------------------------

print('...................................Declaring Variables & Data Types...................................')
print(' ')

# Declaring different types of variables
name = "Alice"        # String
age = 25              # Integer
height = 5.4          # Float
is_student = True     # Boolean

# Displaying the values of these variables using formatted strings
print(f"My name is {name}, I am {age} years old, and I am {height} feet tall.")
print(f"Am I a student? {is_student}")

print(' ')
print('...................................Declaring Variables & Data Types...................................')
print(' ')

# --------------------------------------------------------
# Task 3: Performing Basic Arithmetic Operations
# --------------------------------------------------------

print('...................................Arithmetic Operations...................................')
print(' ')

# Taking input from the user for two numbers
num1 = float(input("Enter the first number: "))  # Convert input to float for decimal operations
num2 = float(input("Enter the second number: "))

# Performing arithmetic operations
sum_result = num1 + num2
difference = num1 - num2
product = num1 * num2
quotient = num1 / num2 if num2 != 0 else "undefined"  # Handling division by zero

# Displaying the results
print(f"The sum of {num1} and {num2} is: {sum_result}")
print(f"The difference when subtracting {num2} from {num1} is: {difference}")
print(f"The product of {num1} and {num2} is: {product}")
print(f"The quotient when dividing {num1} by {num2} is: {quotient}")

print(' ')
print('...................................Arithmetic Operations...................................')
print(' ')

# --------------------------------------------------------
# Task 4: Calculating the Area of a Circle
# --------------------------------------------------------

print('...................................Area of a Circle...................................')
print(' ')

# Asking the user to input the radius of the circle
radius = float(input("Enter the radius of the circle: "))

# Calculating the area of the circle
area = math.pi * radius ** 2  # Area formula: π * r^2

# Displaying the result
print(f"The area of the circle with radius {radius} is: {area:.2f} square units.")

print(' ')
print('...................................Area of a Circle...................................')
print(' ')
