class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        output = 0
        for day in range(len(prices)):
            for i in range(day + 1, len(prices)):
                if prices[i] - prices[day] > output:
                    output = prices[i] - prices[day]

        return output