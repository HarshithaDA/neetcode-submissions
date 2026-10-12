class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # convert array into hashset
        # [1...len(arr)+1] -> check if n belongs to hashset
        # if yes, try n = 2, then so on
        # if no, return n
        # if n = len(arr) return len(arr)+1

        # use input array as memory
        # for every val [1...len(arr)+1] -> mapped to index in array
        # does 2 exist in input array
        # index = 2-1 = 1 go to 1 index check number in array, if -ve, 2 exists else does not
        # replace negative nums by 0
        # for every number in array, for value we want to mark it as exists, so index = |val| - 1 -> go to that index and change value to negative value if already positive
        # if index is out of bounds, do not fill

        # change negative values to 0 in input array
        for i in range(len(nums)):
            if nums[i]<0:
                nums[i] = 0

        # marking that value exists if in bounds
        for i in range(len(nums)):
            val = abs(nums[i])
            if 1 <= val <= len(nums):
                index = val - 1
                # mark that it exists by changing to negative value if that number was positive in the first place
                if nums[index] > 0:
                    nums[index] =  nums[index] * -1

                # if value is 0, change to (len+1 )*-1
                elif nums[index] == 0:
                    nums[index] = -1 * (len(nums) +1)

        # if i is not in input array
        for i in range(1, len(nums)+1):
            # if positive or 0 it did not exist
            if nums[i-1] >= 0:
                return i
        return len(nums)+1

        

