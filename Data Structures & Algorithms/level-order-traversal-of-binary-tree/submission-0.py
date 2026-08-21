# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = collections.deque()
        q.append(root)

        # run bfs while queue is not empty
        while q:
            # no. of values in q currently and loop through them
            qLen = len(q)
            # iterate through one level at  a time
            level = []
            for i in range(qLen):
                # pop nodes from left of q
                node = q.popleft()
                # check to make sure its not null
                if node:
                    level.append(node.val)
                    # add children of this node to the q
                    q.append(node.left)
                    q.append(node.right)
            if level:
                res.append(level)
        return res