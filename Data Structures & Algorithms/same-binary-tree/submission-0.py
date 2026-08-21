# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # empty trees are equal
        if not p and not q:
            return True
        # if one of them is empty return false - not equal immediately
        if not p or not q:
            return False
        # if values of nodes are not equal - not equal 
        if p.val != q.val:
            return False

        # both nodes are non empty and their values are same
        # is the same tree on right and left subtree?

        # we need both these to be true so and them
        return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))