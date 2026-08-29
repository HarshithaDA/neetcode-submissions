class Solution:
    def numDecodings(self, s: str) -> int:
        # if a string starts with  0 - its invalid
        # first digit can be one or two 

        # if its an empty string then we want to return 1 so set initially
        dp = {len(s): 1}

       # i is the position we are at in the string 
        def dfs(i):
            # already been cached or if i at end of string
            if i in dp:
                return dp[i]
            # if string starts with 0 its invalid
            # a-> z 1->26
            if s[i] == "0":
                return 0

            # between 1-9 - we can take as single digit - subproblem
            res = dfs(i+1)

            # checking if this double digit value is between 10-26
            # tens digit is 1 or 2 - cant be 3 has to be less than equal to 26
            # units digit has to be between 0 and 6
            if (i+1 <len(s) and (s[i] == "1" or s[i] == "2" and s[i+1] in "0123456")):
                # double digit - so subproblem i+2
                res += dfs(i+2)
            
            # cache the result
            dp[i]=res
            return res

        # how many ways starting at position 0
        return dfs(0)

