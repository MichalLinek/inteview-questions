class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        stack = [] #ids
        output = []
        for i, val in enumerate(nums):
            if stack and stack[0] + k == i:
                stack.pop(0)
            while stack and nums[stack[-1]] < val:
                stack.pop()
            stack.append(i)
                
            if i >= k - 1:
                output.append(nums[stack[0]])
            
        return output