class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q=deque()
        time, fresh=0,0

        rows=len(grid)
        cols=len(grid[0])

        for i in range(rows):
            for j in range(cols):
                # count number of fresh oranges
                if grid[i][j]==1:
                    fresh+=1
                # rotting orange
                if grid[i][j]==2:
                    # append rotting orange to queue
                    q.append([i, j])

        directions = [[0,1], [0,-1], [1,0], [-1,0]]
        # while we still have fresh oranges
        while q and fresh>0:
                # pop the rotten oranges and add adj oranges to q marking them as rotten
                for i in range(len(q)):
                    # pop from left - not the same ones we are adding
                    r, c = q.popleft()
                    for dr, dc in directions:
                        row, col = dr+r, dc+c
                        # if in bounds and fresh, make it rotten
                        if (row<0 or row==len(grid) or
                            col<0 or col==len(grid[0]) or
                            grid[row][col] != 1):
                            continue
                        grid[row][col]=2
                        q.append([row,col])
                        fresh-=1
                time+=1
        return time if fresh==0 else -1






                    