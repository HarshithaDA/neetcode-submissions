class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        res = max(piles)

        l=1
        r=max(piles)

        while l<=r:
            k = (l+r)//2
            hours = 0

            for p in piles:
                hours += math.ceil(p / k)

            if hours<=h:
                res = min(res, k) 
                # search the left portion 
                r = k-1
            else:
                # search right portion
                l=k+1

        return res

