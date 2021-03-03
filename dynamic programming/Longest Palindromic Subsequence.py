#longest palindromic subsequence

def solve(i, j, string, memo):
    if i > j: return 0
    if i == j: return 1
    if (i, j) in memo: return memo[(i, j)]
    v1 = 0
    v2 = 0
    if string[i] == string[j]:
        v1 = 2 + solve(i + 1, j - 1, string ,memo)
    else:
        v2 = max(solve(i + 1, j, string, memo), solve(i, j - 1, string ,memo))
        
    memo[(i, j)] = max(v1, v2)
    return memo[(i, j)]
        
    
def dp(string):
    n = len(string)
    tab = [[0 for i in range(n)] for i in range(n)]
    
    for i in range(n):
        tab[i][i] = 1
        
    for col in range(1, n):
        for row in range(n - col):
            if string[col + row] == string[row]:
                tab[row][col + row] = 2 + tab[row+1][col + row -1]
            else:
                tab[row][col + row] = max(tab[row+1][col + row], tab[row][col + row - 1])
                
    return tab[0][-1]
    
string = "BAAAAAABCGBAB"
val = solve(0, len(string) -1, string, {})
val2 = dp(string)
print(val)
print(val2)