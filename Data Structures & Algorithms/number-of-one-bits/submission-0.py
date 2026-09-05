class Solution:
    def hammingWeight(self, n: int) -> int:
        # checking if rightmost digit is 1 or 0 -> modulo with 2
        # if ans is 1 then its 1 else its 0 -> 1%2=1 0%2=0
        # how to check other digits? - bit shift operation shift all to right
        ones = 0

        while n>0:
            # check if ones place is 0 or not
            # if its a 1 increment 0
            if n%2 == 1:
                ones+=1
            # shift everything to the right by 1
            n = n >> 1

        return ones

