# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # for each level of the tree, we want the rightmost node
        # bfs 
        # add root to queue
        # have a queue and a result array
        # add children l->r of root to queue and remove the root
        # add root to result
        # add rightmost node to result array

        res = []
        q = collections.deque([root])
        while q:
            # get rightside element
            rightside = None
            # for this level get the length
            qLen = len(q)


            # go thru every element in this level
            for i in range(qLen):
                # and pop it
                # pop from lefft add from right
                node = q.popleft()

                # if node is null, go to the next iteration
                # if not null, update the rightside to the last node that is in the current level
                if node:
                    rightside = node
                    q.append(node.left)
                    q.append(node.right)

            if rightside:

                res.append(rightside.val)

        return res
