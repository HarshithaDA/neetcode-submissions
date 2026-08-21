class Solution:
    def isPalindrome(self, s: str) -> bool:
        mycheck = ''
        for c in s:
            if c.isalnum():
                mycheck = mycheck + c.lower()
        return mycheck == mycheck[::-1]