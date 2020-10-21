class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        d = [0] * k
        for i in arr:
            val = (k - i) % k
            if val == 0: continue
            elif d[val] > 0:
                d[val] -= 1
            else:
                d[k - val] += 1
         
        for i in d:
            if i > 0: return False
        return True