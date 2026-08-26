class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

      # union find algorithm (disjoint sets)
      # tree condition 1 - no cycles
      # tree condition 2 - all nodes have to be connected  

      # pick the last edge in the list to remove and return - cuz thats what completes the cycle 
      # detect if there is a cycle
        n = len(edges)
        visit = set()
        rank = [1] * (n+1)
        par = [i for i in range(n+1)] # ith node -> parent (1-n)

        def find(n1):
            # if parent is same as current return it
            if n1 == par[n1]:
                return par[n1]
                # else find the parent by recurrsion
            par[n1] = find(par[n1])
            return par[n1]

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return False

            # path compression & union by rank
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]

            return True

        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]
