class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # value:index
        prev = {}
        for i, num in enumerate(nums):
            diff=target-num
            if diff in prev:
                return [prev[diff], i]

            # add to hashmap value:index if not yet visited
            prev[num]=i
        return


