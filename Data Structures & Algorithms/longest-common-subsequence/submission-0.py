class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # both strings at row and col - grid
         # bottom up 2d dp 

        # if chars match, 1+ diagonal value down
        # if chars dont match, max(down, right)
        # 2d grid, extra bottom row and right col - initialize to 0
        dp = [[ 0 for j in range(len(text2) + 1)]
                  for i in range(len(text1) + 1)]

        # iterate reverse order
        for i in range(len(text1) -1, -1, -1):
            for j in range(len(text2) -1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1+ dp[i+1][j+1]
                else:
                    dp[i][j] = max(dp[i][j+1], dp[i+1][j])

        return dp[0][0]