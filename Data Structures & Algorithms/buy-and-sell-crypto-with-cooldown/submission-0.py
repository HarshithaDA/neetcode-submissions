class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # state: buying or selling?
        # buy-> i+1
        # sell-> i+2

        dp={} # key=(i, buying_boolean)  val=max_profit

        def dfs(i,buying):
            if i>=len(prices):
                return 0
            
            if (i,buying) in dp:
                return dp[(i, buying)]

            if buying:
                # we can buy or have a cooldown
                buy = dfs(i+1 ,not buying)-prices[i]
                cool= dfs(i+1, buying)
                dp[(i,buying)] = max(buy, cool)

            else:
                # if you sell
                sell=dfs(i+2, not buying) + prices[i]
                cool= dfs(i+1, buying)
                dp[(i,buying)] = max(sell, cool)

            return dp[(i,buying)]
        return dfs(0,True)