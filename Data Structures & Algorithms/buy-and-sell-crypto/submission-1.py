class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_buy = prices[0]
        for day in prices:
            profit = max(profit, day - min_buy)
            min_buy = min(min_buy, day)
        return profit