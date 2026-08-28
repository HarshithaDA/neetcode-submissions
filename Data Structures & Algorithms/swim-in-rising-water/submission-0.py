class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # Dijikstra with some modifications - bfs - minheap
        # we want to minimize the maximum height of all paths
        # we are finding the path with smallest max height
        # min heap (max (own height, height before it), r, c)
        
        n = len(grid)
        visit = set()
        minheap=[[grid[0][0], 0, 0]] # (time/max-height, r, c)
        visit.add((0,0))
        directions = [[0,1], [0,-1], [1, 0], [-1,0]]

        while minheap:
            h, r, c = heapq.heappop(minheap)

            # reached bottom most right corner so return result
            if r==n-1 and c==n-1:
                return h
        
            for dr, dc in directions:
                neirow, neicol = dr+r, dc+c
                if (neirow<0 or neicol<0 or neirow==n or neicol==n or (neirow, neicol) in visit):
                    continue
                visit.add((neirow, neicol))
                heapq.heappush(minheap, [max(h, grid[neirow][neicol]), neirow, neicol])