class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # check if the total length of s1 and s2 matched the length of s3
        if len(s1) + len(s2) != len(s3):
            return False
        # memoization cache
        dp = {}

        def dfs(i, j):
            # both out of bounds, return true
            if i==len(s1) and j==len(s2):
                return True
            # if already in cache return the value directly
            if (i, j) in dp:
                return dp[(i,j)]

                # if i in bounds and does the char in s1 match the char in s3 - if yes increment i by 1 - we used the char in s1
                # target char in string 3 -> i+j
                # if they match we increment i by 1
            if i< len(s1) and s1[i] == s3[i+j] and dfs(i+1, j):
                    return True
                # if j in bounds and does the char in s2 match the char in s3 - if yes increment j by 1 - we used the char in s2
                # target char in string 3 -> i+j
                # if they match we increment j by 1
            if j<len(s2) and s2[j] == s3[i+j] and dfs(i, j+1):
                    return True
                
                # caceh it as false and return as false
            dp[(i,j)] = False
            return False
        return dfs(0,0)
                
