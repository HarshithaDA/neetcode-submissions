class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # memoization - caching the repeated work
        # bottom up dp
        # dfs(index_cointype i , current_amount a)
        # 2d grid - coin & amount
        # rightmost col = 1
        # keep just prev row in memory
        # look (cointype) spots to right and directly below and add them 

        cache = {}

        def dfs(i, a):
            if a == amount:
                return 1
            if a>amount:
                # we cannot sum the amount
                return 0
            # index out of bounds no more coins available
            if i == len(coins):
                return 0
            # if already computed, take res directly from cache
            if (i,a) in cache:
                return cache[(i,a)]

            # 2 dfs call
            # dfs 1- choose coin that is at index i - a + coins[i]
            # dfs 2-  skip coin at index i and increment index by 1
            cache[(i,a)] = dfs(i, a+coins[i]) + dfs(i+1, a)
            
            return cache[(i,a)]

        return dfs(0,0)
            

