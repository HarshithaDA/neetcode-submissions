class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        longest=0
        # check if num is a start of a seq
        for n in nums:
            if (n-1) not in nums:
                # no left neighbour -> means start of a sequence
                length = 0
                while (n+length) in numsSet:
                    length+=1
                longest = max(length, longest)

        return longest

