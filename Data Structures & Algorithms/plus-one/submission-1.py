class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # reverse entire array add then reverse it back to return output
        digits = digits[::-1]
        one = 1
        i = 0

        while one:
            if i<len(digits):
                if digits[i] == 9:
                    # we have a carry
                    digits[i] = 0
                else:
                    # no carry
                    digits[i] += 1
                    one = 0
            else:
                digits.append(1)
                one = 0
            
            i+=1

        return digits[::-1]

