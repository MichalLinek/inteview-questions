class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        tab = [False] * (len(s) + 1)
        tab[0] = True
        
        for i in range(1, len(s) + 1):
            for key in wordDict:
                sol = i - len(key)
                if sol >= 0 and s[sol:i] == key:
                    tab[i] = tab[sol] or tab[i]
        return tab[-1]