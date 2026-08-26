class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # water can only flow to adjacent cell that has lower or equal amount of water than it 
        # need to find if a cell can reach pacific and atlantic oceans, if it can then add to list 
        # do it from the borders of the oceans
        # so from borders, you can go to same value or increasinf value
        # visit hashset
        # from borders run dfs

        rows = len(heights)
        cols = len(heights[0])

        # all positions that can reach the oceans
        pac=set()
        atl=set()

        def dfs(r,c,visit, previousHeight):
            if ((r,c) in visit or r<0 or r==rows or c<0 or c==cols or heights[r][c]<previousHeight):
                return 

            visit.add((r,c))
            # run dfs on all 4 neighbours
            dfs(r+1, c, visit, heights[r][c])
            dfs(r-1, c, visit, heights[r][c])
            dfs(r, c+1, visit, heights[r][c])
            dfs(r, c-1, visit, heights[r][c])


        # every position in 1st row (pacific) 
        for c in range(cols):
            # water can go at equal or greater values/height
            # can always do equal height so give same height as current position
            dfs(0,c, pac, heights[0][c]) 

            # every position in last row - atlantic 
            dfs(rows-1, c, atl, heights[rows-1][c])

        # every posiiotn at 1st (pacific) and last (atlantic) columns
        for r in range(rows):
            dfs(r, 0, pac, heights[r][0])

            dfs(r, cols-1, atl, heights[r][cols-1])

        res=[]
        for r in range(rows):
            for c in range(cols):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c])

        return res






