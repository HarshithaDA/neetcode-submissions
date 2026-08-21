class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows,cols = len(board), len(board[0])
        # to store all values currently in our path so we dont revisit the same twice
        path=set()


        def dfs(r,c,i):
            # i is index of current character within target word we are looking for
            if i==len(word):
                return True
            
            if (r<0 or c<0 or r>=rows or c>=cols or word[i]!=board[r][c] or (r,c) in path):
                return False

            path.add((r,c))
            res=    (dfs(r+1, c, i+1) or
                    dfs(r-1, c, i+1) or
                    dfs(r, c+1, i+1) or
                    dfs(r, c-1, i+1)        
                    )

            path.remove((r,c))
            return res

        for r in range(rows):
            for c in range(cols):
                if dfs(r,c,0):
                    return True
        return False

