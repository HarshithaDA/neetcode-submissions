class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        dp = {} # (r,c) -> LIP

        def dfs(r, c, prevval):
            if (r<0 or r==rows or c<0 or c==cols or matrix[r][c] <= prevval):
                # if out of bounds and not increasing  
                return 0
            
            # if already have lipp return directly
            if (r,c) in dp:
                return dp[(r,c)]

            # length
            res = 1
            # run dfs on all directions
            # only update if its greater than result

            # returns LIC in r+1 ->  dfs(r+1, c, matrix[r][c])
            # length will be 1+ above thing
            res = max(res, 1 + dfs(r+1, c, matrix[r][c]))
            res = max(res, 1 + dfs(r-1, c, matrix[r][c]))
            res = max(res, 1 + dfs(r, c+1, matrix[r][c]))
            res = max(res, 1 + dfs(r, c-1, matrix[r][c]))

            dp[(r,c)] = res
            return res

        for r in range(rows):
            for c in range(cols):
                # row, col, preval
                dfs(r,c,-1)

        return max(dp.values())
            

