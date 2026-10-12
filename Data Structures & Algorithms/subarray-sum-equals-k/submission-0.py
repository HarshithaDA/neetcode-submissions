class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # sum each number in array
        # arr[i] - k = diff
        # check if diff in prefix map, if no, continue and increment count in map for corresponding prefix sum
        # if diff in prefix map, if yes, take diff match to map prefixsum and return the count  and increment the result by the count

        res = 0 
        cursum = 0
        # base case
        prefixsummap = {0:1}

        # for every num in input array, add to cursum
        for n in nums:
            cursum+=n
            # difference
            diff = cursum-k
            # if diff in map, add count to result else add 0 default
            res += prefixsummap.get(diff, 0)
            # increment count in map
            prefixsummap[cursum] = 1 + prefixsummap.get(cursum, 0)

        return res
