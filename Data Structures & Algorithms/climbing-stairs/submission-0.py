class Solution:
    def climbStairs(self, n: int) -> int:
        one = 1
        two = 1
        # we have to compute n-1 values in front
        for i in range(n-1):
            temp = one
            one = one+two
            two = temp
            
        return one