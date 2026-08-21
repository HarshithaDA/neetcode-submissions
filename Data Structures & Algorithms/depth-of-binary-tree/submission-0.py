# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        # our stack contains pair of values the node and the depth
        stack = [[root, 1]]
        res =0

        while stack:
            node, depth = stack.pop()
            if node:
                # update result
                res = max(res, depth)
                # add children of node
                stack.append([node.left, depth+1])
                stack.append([node.right, depth+1])

        return res