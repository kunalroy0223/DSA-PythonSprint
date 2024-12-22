# Day 12: Python Dictionaries

# --------------------------------------------------------
# Task 1: Creating and Accessing Dictionaries
# --------------------------------------------------------

print('...................................Creating and Accessing Dictionaries...................................')

# Creating a dictionary
student = {
    "name": "Alice",
    "age": 22,
    "major": "Computer Science"
}

# Accessing values
print(f"Name: {student['name']}")
print(f"Age: {student['age']}")
print(f"Major: {student['major']}")

# Using .get() to access values safely
print(f"GPA: {student.get('GPA', 'Not Available')}")  # Default value if key doesn't exist

# --------------------------------------------------------
# Task 2: Adding, Updating, and Removing Items
# --------------------------------------------------------

print('...................................Adding, Updating, and Removing Items...................................')

# Adding a new key-value pair
student["GPA"] = 3.8
print(f"Updated Dictionary: {student}")

# Updating an existing key-value pair
student["age"] = 23
print(f"Dictionary after updating age: {student}")

# Removing a key-value pair
student.pop("major")  # Removes the key "major"
print(f"Dictionary after removing major: {student}")

# Using del keyword
del student["GPA"]
print(f"Dictionary after deleting GPA: {student}")

# --------------------------------------------------------
# Task 3: Looping Through a Dictionary
# --------------------------------------------------------

print('...................................Looping Through a Dictionary...................................')

# Iterating through keys and values
for key, value in student.items():
    print(f"{key}: {value}")

# --------------------------------------------------------
# Task 4: Practical Use Case
# --------------------------------------------------------

print('...................................Practical Use Case...................................')

# Counting word occurrences in a string
text = "hello world hello everyone in the world"
word_counts = {}

# Splitting text into words and counting
for word in text.split():
    word_counts[word] = word_counts.get(word, 0) + 1

# Displaying word counts
print(f"Word Counts: {word_counts}")

print('...................................Practical Use Case...................................')
