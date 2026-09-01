class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # add a 1 at begining and end
        nums = [1] + nums + [1]

        dp = {  }

        def dfs(l, r):
            if l>r: # nothing left to pop
                return 0
            if (l,r) in dp: # already cached
                return dp[(l,r)]
            
            dp[(l,r)] = 0
            # find max no. of coins for this pair
            for i in range(l, r+1):
                coins = nums[l-1] * nums[i] * nums[r+1]
                # additional coins from left and right subarrays
                coins += dfs(l, i-1) + dfs(i+1, r)
                dp[(l,r)] = max(dp[(l,r)], coins)
            return dp[(l,r)] 

        # return excluding the first and last values 1 added
        return dfs(1, len(nums)-2)