"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # go to each node and create copy of it
        # but each node can be connected to a node so its recursive
        # once nodes have their clones, we can connect them with an edge (clone node's neighbours)

        # hashmap that maps node to its clone node
        oldToNew = {}

        def dfs(node):
            # check if node already in our hashmap -> it already has a clone so just return 
            if node in oldToNew:
                return oldToNew[node]

            # if not present in hashmap then create a clone
            copy = Node(node.val)
            # add to hashmap -> map old node to clone
            oldToNew[node] = copy
            # make copies every single neighbour of the original node
            for n in node.neighbors:
                # run dfs on neighbour -> that will return in clone of neighbour
                # to that copy node we create above, we take the list of its neighbours and append to it this 
                # 
                copy.neighbors.append(dfs(n))

            return copy

        
        return dfs(node) if node else None
