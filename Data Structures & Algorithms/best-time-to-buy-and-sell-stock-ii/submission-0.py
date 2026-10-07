class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # everytime values are in increasing order - we add the increment to our total profit
        profit = 0

        # every i we compare with thr previous position
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                increment = prices[i]-prices[i-1]
                profit = profit+increment

        return profit