class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # memoization - cache 
        dp = {} # (index, cursum) -> number of ways


        def backtrack(i, cursum):
            # if subproblem already in dict already been computed return it
            if (i, cursum) in dp:
                return dp[(i, cursum)]
            # when i is at end of array
            if i== len(nums):
                if cursum == target:
                    return 1
                else:
                    return 0

            # recursive 2 cases/choices 
            # 1. shift i by 1 and to cursum add the curr number at index i
            # 2. shift i by 1 and to cursum sub the curr number at index i
            dp[(i, cursum)] = (
                backtrack(i+1, cursum + nums[i]) +
                backtrack(i+1, cursum - nums[i])
            )

            return dp[(i, cursum)]

        # index 0, cur sum is o ->returns number of ways
        return backtrack(0,0)