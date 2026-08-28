class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Dijikstras algorithm - shortest path - minheap
        # minheap -> keep track of 2 values: min path length & node
        # path length is total length from source node

        # if a node is not connected to the graph then it cannot send the signal  so we return -1

        # layer by layer bfs, add neighbours to minheap
        # pop value from minheap from the min path value

        # if a node is already in minheap, add another node with the shorter minpath and pop that

        edges = collections.defaultdict(list)

        # constructing adjacency list
        for u, v, w in times:
            # node -> (neighbour node, weight of edge)
            edges[u].append((v, w))

        # path length/weight, node
        minheap = [(0, k)]

        visit=set()

        # last ndoe visited cost that is to be returned
        t=0

        while minheap:
            # pop from minheap while non empty
            pl1, n1 = heapq.heappop(minheap)
            if n1 in visit:
                continue
            visit.add(n1)
            # update path length
            t = max(t, pl1)

            # bfs portion - go thru all neighbours of this node
            # edges store for each node -> neighbour, weight of edge
            for n2, w2 in edges[n1]:
                if n2 not in visit:
                    # path length update
                    heapq.heappush(minheap, (w2+pl1, n2))

        # check for all connected graph or not
        return t if len(visit)==n else -1

            





