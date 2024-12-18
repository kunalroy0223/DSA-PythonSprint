# Day 8: Dictionaries in Python

# --------------------------------------------------------
# Task 1: Creating and Accessing a Dictionary
# --------------------------------------------------------

print('...................................Creating and Accessing a Dictionary...................................')

# Creating a dictionary
student = {
    "name": "Alice",
    "age": 20,
    "grade": "A",
    "subjects": ["Math", "Physics", "Chemistry"]
}

# Accessing dictionary elements
print(f"Student Name: {student['name']}")
print(f"Subjects: {student['subjects']}")

# --------------------------------------------------------
# Task 2: Adding, Updating, and Removing Elements
# --------------------------------------------------------

print('...................................Adding, Updating, and Removing Elements...................................')

# Adding a new key-value pair
student["university"] = "Inspiria Knowledge Campus"
print(f"Updated Dictionary: {student}")

# Updating an existing key
student["grade"] = "A+"
print(f"After Grade Update: {student}")

# Removing a key-value pair
del student["age"]
print(f"After Removing Age: {student}")

# --------------------------------------------------------
# Task 3: Iterating Over a Dictionary
# --------------------------------------------------------

print('...................................Iterating Over a Dictionary...................................')

# Iterating through keys
print("Keys in the dictionary:")
for key in student.keys():
    print(key)

# Iterating through values
print("\nValues in the dictionary:")
for value in student.values():
    print(value)

# Iterating through key-value pairs
print("\nKey-Value Pairs:")
for key, value in student.items():
    print(f"{key}: {value}")

# --------------------------------------------------------
# Task 4: Dictionary Methods
# --------------------------------------------------------

print('...................................Dictionary Methods...................................')

# Using get() to fetch a value with a default fallback
print(f"Major: {student.get('major', 'Not Specified')}")

# Checking if a key exists
if "name" in student:
    print("Key 'name' exists in the dictionary.")

# Clearing a dictionary
temp_dict = {"temp": "value"}
temp_dict.clear()
print(f"Cleared Dictionary: {temp_dict}")

# --------------------------------------------------------
# Task 5: Nested Dictionaries
# --------------------------------------------------------

print('...................................Nested Dictionaries...................................')

# Creating a nested dictionary
class_data = {
    "Student1": {"name": "Bob", "age": 22, "grade": "B"},
    "Student2": {"name": "Alice", "age": 20, "grade": "A"},
    "Student3": {"name": "Eve", "age": 21, "grade": "A-"}
}

# Accessing nested dictionary elements
print(f"Student2's Grade: {class_data['Student2']['grade']}")

# --------------------------------------------------------
# Task 6: Practical Use Case
# --------------------------------------------------------

print('...................................Practical Use Case...................................')

# Word frequency counter
sentence = "Python is fun and Python is powerful"
word_count = {}

# Splitting the sentence into words and counting frequencies
for word in sentence.split():
    word_count[word] = word_count.get(word, 0) + 1

print("Word Frequency Count:")
print(word_count)

print('...................................Practical Use Case...................................')
