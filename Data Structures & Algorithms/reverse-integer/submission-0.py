class Solution:
    def reverse(self, x: int) -> int:

        # ones place -> n % 2
        # get rest of digit (without ones) -> n // 10
        # then repeat to get oens place digit

        # ones digit multiply by 10 then add the tens
        # then repeat

        # if number overflows? - 
        # is reversed integer equal to max integer (chop of the ones digit)
        # if ones digit is greater then return 0

        MIN = -2147483648  # -2^31,
        MAX = 2147483647  #  2^31 - 1

        res = 0

        while x:
            # get ones digit by mod with 10
            digit = int(math.fmod(x, 10)) # python -1 % 10 = 9 (thats y we use helper function )
            # get rest of digit wihtout ones place
            x = int(x/10) # python -1 // 10 = -1 (thats y we use helper function )

            # check if overflows before adding the digit 
            # check if reversed number is greater than max digit (without ones place) or if reversed number is equal to max digit (without ones place) and the units digit is greater than or equal to unites digit of max 
            if (res > MAX // 10 or 
            (res == MAX // 10 and digit >= MAX % 10)):
                return 0

            # same thing - checking if integer is too small
            if (res < MIN // 10 or 
            (res == MIN // 10 and digit <= MIN % 10)):
                return 0

            # if not too small or too large, add the units digit to the rest of the reversed number
            res = (res * 10) + digit

        return res



        