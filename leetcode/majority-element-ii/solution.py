class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        first = None
        second = None
        first_count = 0
        second_count = 0
        
        for i in nums:
            if first is None or i == first:
                first = i
                first_count += 1
            elif second is None or i == second:
                second = i
                second_count += 1
            elif first_count == 0:
                first = i
                first_count = 1
            elif second_count == 0:
                second = i
                second_count = 1
            else:
                first_count -= 1
                second_count -= 1
        
        first_count = 0
        second_count = 0
        for i in nums:
            if i == first: first_count += 1
            if i == second: second_count += 1
        
        l = []
        if first_count > len(nums) /3: l.append(first)
        if second_count > len(nums) /3: l.append(second)
        
        return l
        
                
            
            
            
        