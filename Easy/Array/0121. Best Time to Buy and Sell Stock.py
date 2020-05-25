class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        min_price = float("inf")
        max_profit = 0
        
        for i in prices:
            min_price = min(min_price, i)
            max_profit = max(i - min_price, max_profit)
        
        return max_profit
