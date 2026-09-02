class Solution:
    def checkValidString(self, s: str) -> bool:
        # when right ) is more than left ( -> invalid
        # if leftmin is ever negative -> set it back to 0
        # if rightmin is ever negative -> invalid

        leftmax, leftmin = 0,0

        for c in s:
            if c == "(":
                leftmax, leftmin = leftmax + 1, leftmin + 1
            elif c == ")":
                leftmax, leftmin = leftmax - 1, leftmin - 1
            else: # *
                leftmax, leftmin = leftmax + 1, leftmin - 1

            if leftmax < 0:
                return False
            if leftmin < 0:
                leftmin = 0

        # return True if leftmin == 0
        return leftmin == 0
