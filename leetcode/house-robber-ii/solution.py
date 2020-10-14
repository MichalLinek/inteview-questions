class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums: return 0
        if len(nums) == 1: return nums[0]
        return max(self.solve(nums[:-1]), self.solve(nums[1:]))
        
    def solve(self, nums):
        n = len(nums) + 1
        dp = [0] * n
        dp[1] = nums[0]
        for i in range(2, n):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i - 1])
        return dp[-1]