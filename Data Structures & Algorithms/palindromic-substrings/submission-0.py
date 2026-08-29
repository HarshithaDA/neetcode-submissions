class Solution:
    def countSubstrings(self, s: str) -> int:
        # go thru all substrings where each char is the middle of the substring - expand outward left and right pointers both start at same position
        # we only get palindromes of odd len by the above method
        # to get even len palindromes, left ptr and right ptr will be left +1
        res = 0

        # odd len palindromes
        for i in range(len(s)):
            l,r=i, i
            while l>=0 and r<len(s) and s[l]==s[r]:
                # found a palindrome and l and r are in bounds
                res+=1
                l-=1
                r+=1
            
            # for even palindromes
            l=i
            r=i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
            # found a palindrome and l and r are in bounds
                res+=1
                l-=1
                r+=1

        return res



