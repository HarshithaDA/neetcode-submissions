class Solution:
    def isHappy(self, n: int) -> bool:
        visit = set()

        while n not in visit:

            visit.add(n)
            # compute sum of squares
            n = self.sumofsquares(n)

            if n==1:
                return True

            
        # visited value twice and its not 1
        return False

    def sumofsquares(self, n):
        # ones place -> n%10
        # tens place -> n/10

        output = 0

        while n:
            ones = n%10
            ones = ones ** 2
            output += ones

            n = n//10

        return output

        