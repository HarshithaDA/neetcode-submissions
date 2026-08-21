class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        target = 0

        for i, n in enumerate(nums):
            # do not want to use duplicates in left and right pointers
            # not the first number and left neighbour is the same
            if i>0 and n == nums[i-1]:
                continue

            l = i+1
            r=len(nums)-1
            while l<r:
                curSum = nums[l]+nums[r]+n
                if curSum<target:
                    l=l+1
                if curSum>target:
                    r=r-1
                if curSum == target:
                    res.append([n, nums[l], nums[r]])
                    # only gonna shift left pointer
                    l+=1
                    while nums[l] == nums[l-1] and l<r:
                        # that means its the same value so we keep shifting the pointer and also keep a check that left pointer is always less than right pointer dont want it to pass the right pointer
                        l = l+1 

        return res