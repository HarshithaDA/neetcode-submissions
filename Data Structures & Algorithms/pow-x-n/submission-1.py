class Solution:
    def myPow(self, x: float, n: int) -> float:
        # x^n 
        # x^-n = 1/x^n

        def helper(x, n):

            if n == 0:
                return 1

            if x == 0:
                return 0

            res = helper(x, n // 2)
            res = res * res

            return x * res if n% 2 else res
            # if n is odd, multiple by x one more time        

        res = helper(x, abs(n))
        return res if n>=0 else 1 / res
                # x^-n = 1/x^n

        