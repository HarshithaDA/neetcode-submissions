class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # 2 pointers 
        # ptr1 - iterate through array
        # ptr2 - next time we see a unique value where to put from left side? - also tells us how many unique values we've already seen so far
        
        # how to check if its a unique value or not?
        # compare vaule to previous value (input already in ascending order)

        left = 1
        
        for right in range(1, len(nums)):
            if nums[right] != nums[right-1]:
                nums[left] = nums[right]
                left+=1
        
        return left




        