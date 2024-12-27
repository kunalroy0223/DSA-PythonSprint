# --------------------------------------------------------
# Day 17: Python for Data Structures and Algorithms Challenge
# --------------------------------------------------------

# Topic: Greedy Algorithms

# --------------------------------------------------------
# Task 1: Understanding the Greedy Approach
# --------------------------------------------------------

print('...................................Understanding the Greedy Approach...................................')

# Example Problem: Coin Change Problem (Finding Minimum Coins)
coins = [1, 5, 10, 25]
amount = 63

# Function to calculate minimum coins
def min_coins(coins, amount):
    coins.sort(reverse=True)
    result = []
    for coin in coins:
        while amount >= coin:
            amount -= coin
            result.append(coin)
    return result

# Calculating minimum coins
change = min_coins(coins, amount)
print(f"Coins used to make {63}: {change}")

# --------------------------------------------------------
# Task 2: Activity Selection Problem
# --------------------------------------------------------

print('...................................Activity Selection Problem...................................')

# Example Problem: Selecting Maximum Number of Non-Overlapping Activities
activities = [(1, 3), (2, 5), (4, 6), (6, 7), (5, 9)]
activities.sort(key=lambda x: x[1])  # Sort by finish time

def max_activities(activities):
    selected = [activities[0]]
    last_end_time = activities[0][1]

    for i in range(1, len(activities)):
        if activities[i][0] >= last_end_time:
            selected.append(activities[i])
            last_end_time = activities[i][1]

    return selected

# Calculating the maximum number of activities
result = max_activities(activities)
print(f"Selected Activities: {result}")

# --------------------------------------------------------
# Task 3: Huffman Coding (Data Compression)
# --------------------------------------------------------

print('...................................Huffman Coding...................................')

import heapq

# Example Problem: Huffman Coding
class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def huffman_coding(freq):
    heap = [Node(char, freq[char]) for char in freq]
    heapq.heapify(heap)

    while len(heap) > 1:
        node1 = heapq.heappop(heap)
        node2 = heapq.heappop(heap)
        merged = Node(None, node1.freq + node2.freq)
        merged.left = node1
        merged.right = node2
        heapq.heappush(heap, merged)

    return heap[0]

# Frequency of characters
frequency = {'a': 5, 'b': 9, 'c': 12, 'd': 13, 'e': 16, 'f': 45}
root = huffman_coding(frequency)

# Displaying Huffman Codes
def print_codes(node, code=""):
    if not node:
        return
    if node.char:
        print(f"{node.char}: {code}")
    print_codes(node.left, code + "0")
    print_codes(node.right, code + "1")

print_codes(root)

# --------------------------------------------------------
# Task 4: Practical Use Case
# --------------------------------------------------------

print('...................................Practical Use Case...................................')

# Scheduling tasks with deadlines
tasks = [('A', 2, 100), ('B', 1, 19), ('C', 2, 27), ('D', 1, 25), ('E', 3, 15)]
tasks.sort(key=lambda x: x[2], reverse=True)  # Sort by profit

def job_scheduling(tasks, t):
    n = len(tasks)
    result = [False] * t
    job = ['-1'] * t

    for i in range(n):
        for j in range(min(t - 1, tasks[i][1] - 1), -1, -1):
            if not result[j]:
                result[j] = True
                job[j] = tasks[i][0]
                break
    return job

# Finding the optimal job sequence
optimal_sequence = job_scheduling(tasks, 3)
print(f"Optimal Job Sequence: {optimal_sequence}")

print('...................................Practical Use Case...................................')
