# Day 16: Introduction to Dynamic Programming

# --------------------------------------------------------
# Task 1: Fibonacci Sequence Using Dynamic Programming
# --------------------------------------------------------

print('...................................Fibonacci Sequence Using Dynamic Programming...................................')

# Function to compute Fibonacci numbers using Dynamic Programming
def fibonacci_dp(n):
    # Create an array to store Fibonacci numbers
    fib = [0] * (n + 1)
    fib[1] = 1  # Base case

    # Fill the array using the Fibonacci recurrence relation
    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]

    return fib[n]

# Example: Compute the 10th Fibonacci number
n = 10
result = fibonacci_dp(n)
print(f"The {n}th Fibonacci number is: {result}")

# --------------------------------------------------------
# Task 2: Recursive Approach with Memoization
# --------------------------------------------------------

print('...................................Recursive Fibonacci with Memoization...................................')

# Recursive Fibonacci with memoization (top-down approach)
def fibonacci_memoization(n, memo={}):
    if n in memo:  # Check if the result is already computed
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci_memoization(n - 1, memo) + fibonacci_memoization(n - 2, memo)
    return memo[n]

# Example: Compute the 10th Fibonacci number
result_memo = fibonacci_memoization(n)
print(f"The {n}th Fibonacci number (using memoization) is: {result_memo}")

# --------------------------------------------------------
# Task 3: Practical Use Case - Fibonacci in Real Life
# --------------------------------------------------------

print('...................................Fibonacci Practical Use Case...................................')

# Fibonacci in population growth (example)
print("Population Growth Simulation (Fibonacci Approximation):")
months = 10
rabbit_population = [0] * (months + 1)
rabbit_population[1] = 1  # Start with 1 pair of rabbits

for i in range(2, months + 1):
    rabbit_population[i] = rabbit_population[i - 1] + rabbit_population[i - 2]

print(f"Rabbit population after {months} months: {rabbit_population[months]}")

print('...................................Fibonacci Practical Use Case...................................')
