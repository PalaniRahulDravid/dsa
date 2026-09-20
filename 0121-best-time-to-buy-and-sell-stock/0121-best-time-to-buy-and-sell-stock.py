class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        high = 0
        for i in prices:
            if i<buy:
                buy = i
            profit = i-buy
            if profit>high:
                high = profit
        return high


            