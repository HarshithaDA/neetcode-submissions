class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # when we choose not to use * -> shift j by 2
        # when we choose to use * -> shift i by 1
        # when no * & char match -> increment i & j
        # when i and j out of bounds, perfect match
        # when only j is out of bounds they do not match-return F

        dp = {} 

        def dfs(i,j):
            if (i,j) in dp:
                return dp[(i,j)]
            #  when i and j out of bounds, perfect match
            if i>= len(s) and j>=len(p):
                return True
        # when only j is out of bounds they do not match-return F
            if j >= len(p):
                return False 

            # is there a match between first char of each string
            # . matches to any character
            # i in bounds
            match = i < len(s) and (s[i] == p[j] or p[j] == ".")

            # check if in bounds & does the character match the *
            # 1st char is never a * so start from next position
            if (j+1) < len(p) and p[j+1] == "*":
                # dont use *
                dp[(i,j)] =  (dfs(i, j+2) or
                # use * if there is a match between chars
                (match and dfs(i+1, j))) 

                return dp[(i,j)]

            # if there is a match
            if match:
                dp[(i,j)] = dfs(i+1, j+1)
                return dp[(i,j)]
            return False

        return dfs(0,0)
