class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        l = 0
        r = l + 1
        while r < len(prices):
            if prices[l] > prices[r]:
                l = r
                r = l + 1
            
            else:
                curr_profit = prices[r] - prices[l]
                profit = max(profit, curr_profit)
                r += 1
        return profit
