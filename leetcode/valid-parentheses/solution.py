class Solution:
    def isValid(self, s: str) -> bool:
        
        d = { ')': '(', '}': '{', ']':'['}
        l = []
        for i in s:
            if i in "({[": l.append(i)
            else:
                if len(l) == 0: return False
                if l[-1] == d[i]:
                    l.pop()
                    print('s')
                else:
                    return False
        return len(l) == 0
            