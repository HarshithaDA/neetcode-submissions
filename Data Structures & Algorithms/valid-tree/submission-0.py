class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # trees cannot have loops -> valid tree condition 1
        # every node in tree has to be connected -> valid tree condition 2
        # empty is a valid tree

        # if number of nodes matches the number of nodes visited - then its all connected
        # if no cycle then its valid tree

        # if a neighbour has already been visited, then it will be on visit set but tree may not have a cycle - how to comply with this edge case? - 
        # pass additional parameter prev (the node just visited before curr node) - we are not going back to prev node from this current position
        # root node will have prev set to -1

        # valid tree if no nodes as well
        if not n:
            return True

        # add edges to nodes (undirected so add both ways)
        adj = {i:[] for i in range(n)}

        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        visit = set()

        # passing current and previous nodes
        def dfs(i,prev):
            # if already visited return false
            if i in visit:
                return False

            # if not visited already add to set
            visit.add(i)
            # for all its neighbours 
            for j in adj[i]:
                # j was the previous node we came from skip that list 
                if j == prev:
                    continue
                # else return true if not false
                if not dfs(j, i): return False
            return True

        # starting from root node and it has no previous so set to -1
        # this dfs checks only if there is a cycle
        # add the check for all connected ndoes also
        return dfs(0, -1) and n==len(visit)
            





