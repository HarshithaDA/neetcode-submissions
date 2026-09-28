class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # partition 
        # left pointer starts at left most place
        #  i pointer iterates through the array
        # on iterating thru the array, anytime we get a 0, we swap 0 with the left most value
        # once we have 0 at the lest most, we shift left pointer to the right by 1
        # right pointer starts at right most place
        # everything to right of it is going to be a 2
        # but do not increment i pointer

        l,r = 0, len(nums)-1
        i=0

        def swap(i,j):
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp

        while i<=r:
            if nums[i] == 0:
                swap(l,i)
                l+=1

            elif nums[i] == 2:
                swap(i,r)
                r-=1
                i-=1

            i+=1

        
            




