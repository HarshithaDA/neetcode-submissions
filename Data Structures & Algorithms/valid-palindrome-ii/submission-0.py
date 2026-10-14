class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)  -1 

        # if they meet then we found a palindrome
        while l<r:
            # when not equal, may/may not be a palindrome
            if s[l] != s[r]:
                # skipping left and right characters
                skipl, skipr = s[l+1:r+1], s[l:r]
                # if we skip the left character is it a palindrome?
                # if we skip the right character is it a palindrome?
                # if atleast one of these are ture - return true 
                return (skipl == skipl[::-1] or skipr == skipr[::-1])

            l,r = l+1,r-1

        return True
