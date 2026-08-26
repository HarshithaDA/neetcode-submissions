class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Union Find Algorithm - to count connected compoenets

        # 2 arrays - parent and current
        # initially each node is the parent of itself
        # then connect the ndoes - merge has happened so decrement the counter by 1 (to keep track of connected compoenents)
        # optimizaiton (maintain rank of each node) - to connec the smaller connected comp with the longer connected comp and not the other way around

        # get root parent for both nodes to be connected - if they have different parents they are not already connected
         # if same root parent these are already connected

         # each node is initially the parent of iteself
         # and each has rank 1 initially
        parent = [i for i in range(n)]
        rank = [1] * n

            # find the node's root parent
        def find(n1):
            res = n1

            while res != parent[res]:
                # set parent to grandparetn
                parent[res] = parent[parent[res]]
                res = parent[res]
            return res

        def union(n1, n2):
            # root parents of both nodes
            p1, p2 = find(n1), find(n2)
            # if root parents are same already connected no need to do union/merge
            if p1 == p2:
                return 0

            if rank[p2]>rank[p1]:
                parent[p1] = p2
                rank[p2] += rank[p1]
            else:
                parent[p2] = p1
                rank[p1] += rank[p2]
            return 1 # successful union

        # number of connected comp is iniitally n
        # everytime union is performed we decrement this by 1
        res = n
        for n1, n2 in edges:
            # return value of successful union is 1
            res -= union(n1, n2)
        return res





