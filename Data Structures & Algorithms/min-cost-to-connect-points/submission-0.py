class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # Prims algorithm - Minimum spanning tree - min cost to connect all points
        # cost of edges is the manhatten distance
        # n nodes n-1 edges
        # visit hash set and frontier minheap (pathlen/cost, neighbour/dst node) - we have to pick min cost
        # once all nodes are connected to graph and equal to result we can stop

        # add all neighbours and edges to frontier minheap and
        # pop the min cost node from minheap and add it to visit and add to cost
        
        n = len(points)

        # for each node -> list of [pathlen/cost, neighbour/dst node]
        adj = {i:[] for i in range(n)}

        # get 2 points to compute manhatten distance
        # point to every other point distance thats why i+1
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i+1, n):
                x2, y2 = points[j]
                dist = abs(x1-x2)+abs(y1-y2)

                # both edges
                adj[i].append([dist, j])
                adj[j].append([dist, i])

        # Prims algorithm
        res = 0
        visit=set()
        minheap = [[0,0]] # (pathlen/cost, neighbour/dst node)

        while len(visit)<n:
            cost, node = heapq.heappop(minheap)
            if node in visit:
                continue
            res+=cost
            visit.add(node)

            # go thru all its neighbours
            for neicost, neig in adj[node]:

                if neig not in visit:
                    heapq.heappush(minheap, [neicost, neig])

        return res


