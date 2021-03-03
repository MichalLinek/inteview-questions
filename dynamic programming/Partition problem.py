#Partition problem

arr = [1, 5, 3]

def solve(arr, i, target_sum, memo):
    if i == len(arr): return False
    if (i, target_sum) in memo: return memo[(i, target_sum)]
    if target_sum == 0: return True
        
    memo[(i, target_sum)] = solve(arr, i + 1, target_sum - arr[i], memo) or solve(arr, i + 1, target_sum, memo)
    return memo[(i, target_sum)]
    
arr_sum = sum(arr)
if arr_sum % 2 != 0: print(False)
else: print(solve(arr, 0, arr_sum//2, {}))