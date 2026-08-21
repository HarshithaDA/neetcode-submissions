class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        subset = []


        #[1,2,3] index 0,1,2

        def dfs(i):
            if i>=len(nums):
                res.append(subset.copy())
                # if index is out of bounds
                return


            # decision to inclide nums[i]
            subset.append(nums[i])
            dfs(i+1)

            # decision to not inclide nums[i]
            subset.pop()
            dfs(i+1)

        dfs(0)
        return res