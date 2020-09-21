class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        cap = [0] * 1000
        for trip in trips:
            cap[trip[1]] += trip[0]
            cap[trip[2]] -= trip[0]
        
        curr_cap = 0
        for c in cap:
            curr_cap += c
            if curr_cap > capacity: return False
        return True