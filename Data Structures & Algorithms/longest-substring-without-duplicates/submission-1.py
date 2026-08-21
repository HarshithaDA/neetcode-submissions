class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        charSet = set()
        l=0
        res=0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l+=1
            charSet.add(s[r])
            res=max(res, r-l+1)
        return res

# sliding window
# remove from left - start shrinking when you find duplicate
# find if we have a duplicate by using a set
# remove char from set and window