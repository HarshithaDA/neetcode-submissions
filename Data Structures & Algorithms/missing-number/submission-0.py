class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # xor 0 ^ 1 = 1   1 ^ 1 = 0   0 ^ 0 = 0 
        # 5 ^ 3 ^ 5 = 3
        # apply xor with the input array and the range of len array
        # matched are going to cancel out, only remaining in array is output

        # add end value of nums
        res = len(nums)

        for i in range(len(nums)):
            res = res + (i-nums[i])

        return res