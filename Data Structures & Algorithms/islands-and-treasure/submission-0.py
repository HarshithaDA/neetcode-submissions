class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # simultaneously do a bfs from treasure at the same time
        # bfs solutions are implemented using queues
        # increment distance by 1 everytime we increase and go to the next level in bfs
        # have a visit set so we dont visit the same position multiple times

        rows = len(grid)
        cols = len(grid[0])

        visit= set()
        # q holds treasure cells
        q = deque()

        def addcell(r,c):
            if (r<0 or r==rows or c<0 or c==cols or (r,c) in visit or grid[r][c] == -1):
                # not adding this cell 
                return 
            
            visit.add((r,c))
            q.append((r,c))



        for r in range(rows):
            for c in range(cols):
                # if cell has treausre add to queue and to visit set
                if grid[r][c]==0:
                    q.append((r,c))
                    visit.add((r,c))


        dist=0
        # pop the treasure cells one by one and run bfs
        while q:
            for i in range(len(q)):
                # pop from q and get the first layer of treasure
                r, c = q.popleft()

                # for each treasure, set to current distance
                grid[r][c] = dist

                # then call bfs on all 4 directions
                # add all adjacent 4 cells to queue
                directions = [[1,0], [-1,0], [0,1], [0,-1]]
                for dr,dc in directions:
                        addcell(r+dr, c+dc)

            # moving to next layer in bfs
            dist += 1
