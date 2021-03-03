#Longest bitonic subsequence

def solve(arr, i,increasing, memo):
    if i < 0 : return 0
    if (i, increasing) in memo: return memo[(i, increasing)]
    
    output = 1 
    for j in range(i):
        val = solve(arr, j, increasing, memo)
        if arr[i] > arr[j] and increasing:
            output = max(output, 1 + val)
        elif arr[i] < arr[j] and not increasing:
            output = max(output, 1 + val)
        
    memo[(i, increasing)] = output
    return output

def solve2(arr):
    n = len(arr)
    dp = [[1, 1] for i in range(n)]
    
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i][0] = max(dp[i][0], 1 + dp[j][0])
            elif arr[i] < arr[j]:
                dp[i][1] = max(dp[i][1], 1 + dp[j][1], 1 + dp[j][0])
    o = 0
    for i in range(n):
        o = max(o, dp[i][0], dp[i][1])
    return o

def two_lis(arr):
    n = len(arr)
    dp1 = [1 for i in range(n)]
    dp2 = [1 for i in range(n)]

    for i in range(n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp1[i] = max(dp1[i], 1 + dp1[j])
                
    for i in range(n-1, -1, -1):
        for j in range(i, n):
            if arr[i] > arr[j]:
                dp2[i] = max(dp2[i], 1 + dp2[j])            
    m = 0
    for i in range(n):
        m = max(m, dp1[i] + dp2[i] - 1)
    return m

arr = [3, 1, 6, 4, 3, 2, 0, 3]
memo = {}
print(solve2(arr))
print(two_lis(arr))