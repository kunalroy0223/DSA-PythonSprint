# Day 14: Python Dictionaries

# --------------------------------------------------------
# Task 1: Creating and Accessing Dictionaries
# --------------------------------------------------------

print('...................................Creating and Accessing Dictionaries...................................')

# Creating a dictionary
student_info = {
    "name": "John Doe",
    "age": 21,
    "major": "Computer Science",
    "grades": [85, 90, 78]
}

# Accessing dictionary elements
print(f"Student Name: {student_info['name']}")
print(f"Student Age: {student_info['age']}")
print(f"Student Major: {student_info['major']}")
print(f"Student Grades: {student_info['grades']}")

# Adding a new key-value pair
student_info["year"] = "Senior"
print(f"Updated Student Info: {student_info}")

# --------------------------------------------------------
# Task 2: Dictionary Methods
# --------------------------------------------------------

print('...................................Dictionary Methods...................................')

# Using dictionary methods
keys = student_info.keys()
values = student_info.values()
items = student_info.items()

print(f"Keys: {keys}")
print(f"Values: {values}")
print(f"Items: {items}")

# --------------------------------------------------------
# Task 3: Updating and Removing Items
# --------------------------------------------------------

print('...................................Updating and Removing Items...................................')

# Updating a value
student_info["age"] = 22
print(f"Updated Age: {student_info['age']}")

# Removing an item
student_info.pop("year")
print(f"Dictionary after removing 'year': {student_info}")

# --------------------------------------------------------
# Task 4: Practical Use Case
# --------------------------------------------------------

print('...................................Practical Use Case...................................')

# Word count example
sentence = "this is a test this is only a test"
word_count = {}
for word in sentence.split():
    word_count[word] = word_count.get(word, 0) + 1

print(f"Word Count: {word_count}")

print('...................................Practical Use Case...................................')
