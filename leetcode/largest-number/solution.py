from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        s = list(map(str, nums))
        s.sort(key=cmp_to_key(self.sortfunc))
        return str(int("".join(s)))
    
    def sortfunc(self,x, y):
        n = int(x + y)
        m = int(y + x)
        return 1 if m > n else -1
    
    
    