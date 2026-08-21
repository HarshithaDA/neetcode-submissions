# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # member variable inside this class
        # diameter
        self.res =0

        # returns height
        # recursive dfs
        def dfs(curr):

            # base case -> reached null node -> height of that is just 0
            if not curr:
                return 0

            # recursive dfs on left subtree - need height of leftsubtree
            left = dfs(curr.left)
            # and for right
            right = dfs(curr.right)

            # update diameter result
            self.res = max(self.res, left+right)
            # for max of height plus curr node
            return 1+max(left, right)

            # return height of tree from curr
        dfs(root)
        return self.res
