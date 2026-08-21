# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        curr = root

        while curr:
            if p.val > curr.val and q.val> curr.val:
                # in right subtree
                curr = curr.right
            elif p.val<curr.val and q.val<curr.val:
                # in left subtree
                curr = curr.left
            else:
                # where split occurs - share same root
                return curr



        