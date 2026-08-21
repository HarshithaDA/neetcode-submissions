class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Brute Force
        # res = 0

        # for lpt in range(len(heights)):
        #     for rpt in range(lpt + 1, len(height)):
        #         area = (rpt - lpt)* min(heights[rpt], heights[lpt])
        #         res = max(res, area)

        # return res

        res = 0
        l = 0
        r = len(heights)-1

        while l<r:
            area = (r-l)* min(heights[r], heights[l])
            res = max(area, res)

            if heights[l]<heights[r]:
                l=l+1
            elif heights[l]>heights[r]:
                r=r-1
            else: # l=r increment either one
                r=r-1

        return res



