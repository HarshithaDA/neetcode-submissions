class Solution:
    def reverseBits(self, n: int) -> int:
        # and & it with a 1 to decide if the digit is a 1 or a 0
        # 1 & 1 = 1   0 & 1 = 0
        # shift bits to left for calculating other digits

        # in res array if we have a 1, shift to left by 31 and do or

        res =  0 

        for i in range(32):
            bit = (n >> i) & 1

            # update at reverse order
            res = res | (bit << (31 - i))

        return res
