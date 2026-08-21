class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()


        def backtrack(i,subset):
            if i==len(nums):
                # append a copy of the array created
                res.append(subset[::])
                return

            # all subsets that include nums[i]
            subset.append(nums[i])
            backtrack(i+1, subset)
            subset.pop()

            # dont include nums[i]
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            backtrack(i+1,subset)
        backtrack(0,[])
        return res

