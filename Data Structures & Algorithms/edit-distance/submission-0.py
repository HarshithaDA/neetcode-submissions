class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # 2d array
        dp = [ [float("inf")] * (len(word2) + 1) for i in range(len(word1) + 1)]

        # fill up bottom row, each time sub by j value
        for j in range(len(word2)+1):
            dp[len(word1)][j] = len(word2) - j

        # fill up rightmost col, each time sub by i value
        for i in range(len(word1)+1):
            dp[i][len(word2)] = len(word1) - i

        # bottom up approch
        for i in range(len(word1) -1, -1, -1):
            for j in range(len(word2) -1, -1, -1):
                # if both chars are equal, increment both ptrs
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i+1][j+1]
                # if not matching - 3 operations(insert, delete, replace)
        # if inserting insert char of w2 to w1 - note i pointer at w1 remains - have to check for tht char next - but shift j pointer 

        # if deleting - leave j, i will shift by 1
        # if replacing - increment both pointers
        # if both chars are empty we are done so return operations
                else:
                    dp[i][j] = 1 + min(dp[i+1][j], dp[i][j+1], dp[i+1][j+1])

        return dp[0][0]

