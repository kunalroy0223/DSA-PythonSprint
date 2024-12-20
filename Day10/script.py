# Day 10: Python Dictionaries

# --------------------------------------------------------
# Task 1: Creating and Accessing Dictionaries
# --------------------------------------------------------

print('...................................Creating and Accessing Dictionaries...................................')

# Creating a dictionary
student = {
    "name": "Alice",
    "age": 22,
    "major": "Computer Science",
    "GPA": 3.8
}
print(f"Student Dictionary: {student}")

# Accessing values using keys
print(f"Student's Name: {student['name']}")
print(f"Student's Age: {student['age']}")

# Using the get method
print(f"Student's Major: {student.get('major')}")
print(f"Student's Minor (default): {student.get('minor', 'Not Specified')}")

# --------------------------------------------------------
# Task 2: Updating and Adding Key-Value Pairs
# --------------------------------------------------------

print('...................................Updating and Adding Key-Value Pairs...................................')

# Updating a value
student["GPA"] = 3.9
print(f"Updated GPA: {student['GPA']}")

# Adding a new key-value pair
student["minor"] = "Mathematics"
print(f"Updated Student Dictionary: {student}")

# --------------------------------------------------------
# Task 3: Removing Key-Value Pairs
# --------------------------------------------------------

print('...................................Removing Key-Value Pairs...................................')

# Removing a key-value pair using pop
removed_value = student.pop("minor", None)
print(f"Removed 'minor': {removed_value}")
print(f"Dictionary after removal: {student}")

# Removing the last inserted key-value pair using popitem
last_removed = student.popitem()
print(f"Last Removed Pair: {last_removed}")
print(f"Dictionary after last removal: {student}")

# --------------------------------------------------------
# Task 4: Iterating Over a Dictionary
# --------------------------------------------------------

print('...................................Iterating Over a Dictionary...................................')

# Iterating over keys
print("Keys:")
for key in student.keys():
    print(key)

# Iterating over values
print("Values:")
for value in student.values():
    print(value)

# Iterating over key-value pairs
print("Key-Value Pairs:")
for key, value in student.items():
    print(f"{key}: {value}")

# --------------------------------------------------------
# Task 5: Practical Use Case
# --------------------------------------------------------

print('...................................Practical Use Case...................................')

# Counting word occurrences in a string
sentence = "Python is fun and learning Python is exciting"
word_count = {}

# Splitting the sentence into words and counting occurrences
for word in sentence.split():
    word_count[word] = word_count.get(word, 0) + 1

print(f"Word Count: {word_count}")

print('...................................Practical Use Case...................................')
