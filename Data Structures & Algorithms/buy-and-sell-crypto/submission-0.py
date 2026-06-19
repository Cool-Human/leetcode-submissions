class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(len(prices) - 1):
            j = i + 1
            while j < len(prices):
                if prices[j] - prices[i] > max_profit:
                    max_profit = prices[j] - prices[i]
                j += 1
        return max_profit