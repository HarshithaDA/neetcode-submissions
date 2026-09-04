class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # build output as an array then convert back to string and return 
        # reverse order computation
        # ones place -> n%10
        # carry -> n//10

        if "0" in [num1, num2]:
            return "0"

        # allocate array
        res = [0] * (len(num1)+len(num2))
        # reverse
        num1,num2 = num1[::-1], num2[::-1]

        for i1 in range(len(num1)):
            for i2 in range(len(num2)):
                digit = int(num1[i1]) * int(num2[i2])
                # add the units digit to the current digit
                res[i1+i2] += digit
                # add carry value to next position 
                res[i1+i2+1] += (res[i1+i2]//10)
                res[i1+i2] = res[i1+i2] % 10
        # reverse the result array
        res = res[::-1]
        beg = 0

        # get rid of leading 0s
        while beg < len(res) and res[beg] == 0:
            # increment ptr till we do not have 0s
            beg+=1

        # remove leading 0s
        res = map(str, res[beg:])
        # return as string
        return "".join(res)