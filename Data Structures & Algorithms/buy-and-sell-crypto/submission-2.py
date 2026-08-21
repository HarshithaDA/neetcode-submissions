class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=0 #buy
        r=1 # sell
        maxprofit=0

        while r<len(prices):
            if prices[l]<prices[r]:
                # profitable transaction
                profit = prices[r]-prices[l]
                maxprofit=max(maxprofit, profit)
            else:
                l=r
            r+=1
        return maxprofit
