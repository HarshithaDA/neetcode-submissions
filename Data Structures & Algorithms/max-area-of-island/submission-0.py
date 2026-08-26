class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # run dfs on every island
        # if you see a 1 then run dfs on island and find area of island
        # to not run dfs on the same island multiple times, we use visit=set

        rows = len(grid)
        cols= len(grid[0])
        visit=set()

        def dfs(r,c):
            # if row is out of bound, if column is out of bound, if we have already visited that island, if the grid cell is water -> continue we did not find an island so return area as 0 and add that row col to hashset
            if (r<0 or r==rows or c<0 or c==cols or grid[r][c]==0 or (r,c) in visit):
                return 0
            
            visit.add((r,c))

            # calculate area of island

            # current cell that we are at counts as 1
            res = 1
            # then call dfs on all 4 directions
            directions = [[1,0], [-1,0], [0,1], [0,-1]]
            for dr,dc in directions:
                    res += dfs(r+dr, c+dc)
            return res
       
       
        area=0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1 and (r,c) not in visit:
                    area=max(area, dfs(r,c))

        return area


        