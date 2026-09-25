class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # reassign result if count becomes 0
        # decrement count if you see a different number
        # increment count if you see the same number
        # return result

        res, count = 0,0

        for n in nums:
            if count == 0:
                res=n
           
            count += (1 if n == res else -1)
        return res

