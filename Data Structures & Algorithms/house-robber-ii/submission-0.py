class Solution:
    def rob(self, nums: List[int]) -> int:
        # run house robber one on all except last value
        # run house robber one on all except first value 
        return max(nums[0],self.helper(nums[1:]), self.helper(nums[:-1]))

        # if input array has only 1 value, 1st house by itself - so add that to max


        # house robber 1 solution
    def helper(self,nums):
            rob1, rob2 = 0,0

            for n in nums:
                # max we can rob up until value n
                #[rob1, rob2, n, n+1, ..]
                temp = max(rob1+n, rob2)
                rob1=rob2
                rob2=temp

            return rob2

