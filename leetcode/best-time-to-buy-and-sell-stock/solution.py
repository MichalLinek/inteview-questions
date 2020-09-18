class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        profit = 0
        min_price = prices[0]
        for i in prices:
            profit = max(i - min_price, profit)
            min_price = min(min_price, i)
        
        return profit