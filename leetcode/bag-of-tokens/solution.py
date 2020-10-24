class Solution:
    def bagOfTokensScore(self, tokens: List[int], P: int) -> int:
        n = len(tokens)
        if n == 0: return 0
        tokens.sort()
        
        left = 0
        right = n -1
        output = 0 
        current = 0
        while left <= right:
            if P >= tokens[left]:
                current += 1
                P -= tokens[left]
                left += 1
            elif current <= 0: left += 1
            else:
                P += tokens[right]
                current -= 1
                right -= 1
            output = max(output, current)
        return output