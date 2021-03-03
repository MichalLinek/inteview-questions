#rod cutting

def solve(length, prices, memo):
    if length == 0: return 0
    if length < 0: return -10**6
    if length in memo: return memo[length]
    
    val = 0
    for i in range(len(prices)):
        curr_len = i + 1
        val = max(val, prices[i] + solve(length - curr_len, prices, memo))
    
    memo[length] = val
    return memo[length]


rod_len = 8 
prices = [3 ,  5   ,8,   9  ,10 , 17  ,17,  20]

print(solve(rod_len, prices, {}))


