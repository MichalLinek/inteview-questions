#Maximum Sum Increasing Subsequence
def solve(arr, n):
    output = 0
    dp = [0 for i in range(n)]
    for i in range(n):
        dp[i] = arr[i]
    for i in range(1, n):
        for j in range(i):
            if dp[i] > dp[j]:
                dp[i] = max(dp[i], arr[i] + dp[j])
            
    output = max(dp)
    return output
    
def solve2(arr, i, memo):
    global maks
    if i < 0: return 0
    if i in memo: return memo[i]
    
    output = arr[i]
    for j in range(i):
        val = solve2(arr, j,memo)
        maks = max(maks, val)
        if arr[i] > arr[j]: 
            output = max(output, arr[i] + solve2(arr, j, memo))
    
    memo[i] = output
    return memo[i]

maks = 0
arr = [1, 101, 2, 3, 102, 4, 5] 
memo = {}
solve2(arr, len(arr) -1 , {})
print(maks)
print(solve(arr, len(arr) - 1))  