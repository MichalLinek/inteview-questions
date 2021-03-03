#Palindrome Partitioning

string = 'abcde'

def solve(string, left, right, memo):
    if left >= right: return 0
    if (left, right) in memo: return memo[(left, right)]
    
    #if palindrome:
    is_palindrome = True
    i = left
    j = right
    while i < j:
        if string[i] != string[j]:
            is_palindrome = False
            break
        i += 1
        j -= 1
       
    if is_palindrome:
        print(left, right)
        memo[(left, right)] = 0
        return 0
    
    output = 10000
    for i in range(left, right):
        output = min(output, 1 + solve(string, left, i, memo) + solve(string, i + 1, right, memo))
    memo[(left, right)] = output
    return output
    
    
print(solve(string, 0, len(string) - 1, {}))