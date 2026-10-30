class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # sliding window 

        window = set()
        l = 0

        for r in range(len(nums)):
            # check if window is too large
            # if it is remove the left most value and increment left pointer
            if (r-l) > k:
                window.remove(nums[l])
                l+=1
            # check if num already been added to window
            # if yes, we found a duplicate
            if nums[r] in window:
                return True
            # if no duplicate found, add number to window hashset
            window.add(nums[r])

        return False

