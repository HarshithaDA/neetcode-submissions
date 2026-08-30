class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curmin, curmax = 1,1

        for n in nums:
            # reached 0 value - ignore it so product does nto become 0
            if n == 0:
                # reset everything to 1
                curmin, curmax = 1,1
                continue

            # recompute current max and min
            temp = curmax*n
            curmax = max(n*curmax, n*curmin, n) 
            curmin = min(temp, n*curmin, n)
            res = max(res, curmax, curmin)


        return res


            