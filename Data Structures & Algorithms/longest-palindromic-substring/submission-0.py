class Solution:
    def longestPalindrome(self, s: str) -> str:
        res=""
        reslen=0
        # expand outward to check palindromes
        for i in range(len(s)):
            # odd length palindrome
            # i is the center position right now
            l,r = i,i
            # while a palindrome and inbound
            while l>=0 and r<len(s) and s[l]==s[r]:
                if (r-l+1)>reslen:
                    # if we found a longer palin we update the current length and the palindrome
                    res = s[l:r+1]
                    reslen=r-l+1
                    # left ptr to left and right ptr to right
                l-=1
                r+=1
            # even length
            l, r= i, i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                    if (r-l+1)>reslen:
                        res = s[l:r+1]
                        reslen=r-l+1
                    l-=1
                    r+=1
        return res
                    
