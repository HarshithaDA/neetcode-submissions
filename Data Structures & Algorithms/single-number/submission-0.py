class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hashmap = {} # number, count

        for n in nums:
            # hashmap[key].append(value)
            if n in hashmap:
                hashmap[n]+=1
            else:
                hashmap[n] = 1

        for num,count in hashmap.items():
            if count == 1:
                return num