# --------------------------------------------------------  
# Task 1: Fibonacci Sequence Using Dynamic Programming  
# --------------------------------------------------------  

print('...................................Fibonacci Sequence Using Dynamic Programming...................................')  

# Using a bottom-up approach to calculate Fibonacci numbers  
def fibonacci(n):  
    dp = [0] * (n + 1)  
    dp[1] = 1  

    for i in range(2, n + 1):  
        dp[i] = dp[i - 1] + dp[i - 2]  

    return dp[n]  

n = int(input("Enter the position (n) for Fibonacci sequence: "))  
print(f"Fibonacci number at position {n}: {fibonacci(n)}")  

# --------------------------------------------------------  
# Task 2: Longest Common Subsequence (LCS)  
# --------------------------------------------------------  

print('...................................Longest Common Subsequence (LCS)...................................')  

def lcs(X, Y):  
    m = len(X)  
    n = len(Y)  
    dp = [[0] * (n + 1) for _ in range(m + 1)]  

    for i in range(1, m + 1):  
        for j in range(1, n + 1):  
            if X[i - 1] == Y[j - 1]:  
                dp[i][j] = dp[i - 1][j - 1] + 1  
            else:  
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])  

    return dp[m][n]  

X = input("Enter the first string: ")  
Y = input("Enter the second string: ")  
print(f"Length of Longest Common Subsequence: {lcs(X, Y)}")  

# --------------------------------------------------------  
# Task 3: Knapsack Problem (0/1 Knapsack)  
# --------------------------------------------------------  

print('...................................0/1 Knapsack Problem...................................')  

def knapsack(W, wt, val, n):  
    dp = [[0] * (W + 1) for _ in range(n + 1)]  

    for i in range(1, n + 1):  
        for w in range(1, W + 1):  
            if wt[i - 1] <= w:  
                dp[i][w] = max(dp[i - 1][w], val[i - 1] + dp[i - 1][w - wt[i - 1]])  
            else:  
                dp[i][w] = dp[i - 1][w]  

    return dp[n][W]  

n = int(input("Enter the number of items: "))  
wt = list(map(int, input("Enter the weights of the items: ").split()))  
val = list(map(int, input("Enter the values of the items: ").split()))  
W = int(input("Enter the maximum weight capacity of the knapsack: "))  
print(f"Maximum value in the knapsack: {knapsack(W, wt, val, n)}")  

# --------------------------------------------------------  
# Task 4: Practical Use Case - Subset Sum Problem  
# --------------------------------------------------------  

print('...................................Subset Sum Problem...................................')  

def subset_sum(nums, target):  
    dp = [False] * (target + 1)  
    dp[0] = True  

    for num in nums:  
        for i in range(target, num - 1, -1):  
            dp[i] |= dp[i - num]  

    return dp[target]  

nums = list(map(int, input("Enter the set of numbers: ").split()))  
target = int(input("Enter the target sum: "))  
print(f"Is it possible to achieve the target sum? {'Yes' if subset_sum(nums, target) else 'No'}")  

print('...................................Subset Sum Problem...................................')  
