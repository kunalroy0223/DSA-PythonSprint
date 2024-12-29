# --------------------------------------------------------  
# Task 1: Minimum Edit Distance  
# --------------------------------------------------------  

print('...................................Minimum Edit Distance...................................')  

def min_edit_distance(str1, str2):  
    m, n = len(str1), len(str2)  
    dp = [[0] * (n + 1) for _ in range(m + 1)]  

    for i in range(m + 1):  
        for j in range(n + 1):  
            if i == 0:  
                dp[i][j] = j  
            elif j == 0:  
                dp[i][j] = i  
            elif str1[i - 1] == str2[j - 1]:  
                dp[i][j] = dp[i - 1][j - 1]  
            else:  
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])  

    return dp[m][n]  

str1 = input("Enter the first string: ")  
str2 = input("Enter the second string: ")  
print(f"Minimum Edit Distance between '{str1}' and '{str2}': {min_edit_distance(str1, str2)}")  

# --------------------------------------------------------  
# Task 2: Subset Sum Problem  
# --------------------------------------------------------  

print('...................................Subset Sum Problem...................................')  

def subset_sum(arr, target):  
    n = len(arr)  
    dp = [[False] * (target + 1) for _ in range(n + 1)]  

    for i in range(n + 1):  
        dp[i][0] = True  

    for i in range(1, n + 1):  
        for j in range(1, target + 1):  
            if arr[i - 1] <= j:  
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - arr[i - 1]]  
            else:  
                dp[i][j] = dp[i - 1][j]  

    return dp[n][target]  

arr = list(map(int, input("Enter the array elements: ").split()))  
target = int(input("Enter the target sum: "))  
print(f"Is there a subset with sum {target}? {'Yes' if subset_sum(arr, target) else 'No'}")  

# --------------------------------------------------------  
# Task 3: Egg Dropping Puzzle  
# --------------------------------------------------------  

print('...................................Egg Dropping Puzzle...................................')  

def egg_dropping(eggs, floors):  
    dp = [[0] * (floors + 1) for _ in range(eggs + 1)]  

    for i in range(1, eggs + 1):  
        for j in range(1, floors + 1):  
            if i == 1:  
                dp[i][j] = j  
            elif j == 1:  
                dp[i][j] = 1  
            else:  
                dp[i][j] = 1 + min(max(dp[i - 1][x - 1], dp[i][j - x]) for x in range(1, j + 1))  

    return dp[eggs][floors]  

eggs = int(input("Enter the number of eggs: "))  
floors = int(input("Enter the number of floors: "))  
print(f"Minimum number of trials required: {egg_dropping(eggs, floors)}")  

print('...................................Egg Dropping Puzzle...................................')  
