class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # 0... amount
        dp = [amount + 1]* (amount +1)
        # can also be [float("inf")]* (amount +1)

        # to compute amount 0 we return 0
        dp[0]=0

        # for every amount, 1 to amount
        for a in range(1, amount+1):
            for c in coins:
                # non negative
                if a-c >=0:
                    dp[a] = min(dp[a], 1 + dp[a-c])
                    # coin = 4
                    # a = 7
                    # dp[a-c]=dp[3]
                    # we need min number fo coins so min

        # cannot be equal to the default amount
        return dp[amount] if dp[amount] !=amount+1 else -1


