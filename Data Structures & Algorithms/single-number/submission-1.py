class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        # solution  O(1) space O(n) time
        # bit manipulation
        #a ^ a = 0 (a number XORed with itself is 0)
        #a ^ 0 = a (a number XORed with 0 is itself)
        res = 0
        for n in nums:
            res = n ^ res
        return res


        # solution O(n) time O(n) space
        # hashset
        # removes all duplicates automatically
        # just return hashset as the output
        # seen = set()
        # for num in nums:
        #     if num in seen:
        #         seen.remove(num)
        #     else:
        #         seen.add(num)
        # return list(seen)[0]


        # solution O(n) time O(n) space
        # hashmap = {} # number, count

        # for n in nums:
        #     # hashmap[key].append(value)
        #     if n in hashmap:
        #         hashmap[n]+=1
        #     else:
        #         hashmap[n] = 1

        # for num,count in hashmap.items():
        #     if count == 1:
        #         return num