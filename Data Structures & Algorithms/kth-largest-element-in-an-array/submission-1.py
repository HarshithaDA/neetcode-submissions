class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k=len(nums)-k

        def quickSelect(l,r):
            while l <= r:
                pivot, p=nums[r], l
                for i in range(l,r):
                    if nums[i]<= pivot:
                        # swap p and i
                        nums[p], nums[i] = nums[i], nums[p]
                        p=p+1
                # swap pivot with p index
                nums[p], nums[r] = nums[r], nums[p]

                if k<p:
                    # run quick select on left partition
                    r = p - 1
                elif k>p:
                    l = p + 1
                else: 
                    return nums[p]

        return quickSelect(0, len(nums)-1)