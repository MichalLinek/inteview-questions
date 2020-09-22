class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        for i in range(1, n//2 + 1):
            k = s[0:i] * (n // i) 
            if k == s: return True
        return False