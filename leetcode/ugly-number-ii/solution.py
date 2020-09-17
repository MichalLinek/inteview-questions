class Solution:
    def nthUglyNumber(self, n: int) -> int:
        l1 = []
        l2 = []
        l3 = []
        
        i = 1
        min_value = 1
        while i < n:
            
            l1.append(min_value * 2)
            l2.append(min_value * 3)
            l3.append(min_value * 5)
            
            min_val = min(l1[0], l2[0], l3[0])
            if l1[0] == min_val: l1.pop(0)
            if l2[0] == min_val: l2.pop(0)
            if l3[0] == min_val: l3.pop(0)
            
            min_value = min_val
            
            print(min_value)
            i += 1
            
        return min_value