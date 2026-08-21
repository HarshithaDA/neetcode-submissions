# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # if subtree is empty then the subtree is in the tree
        if not subRoot: return True
        # if  opposite is true its fallse
        if not root: return False

        # if both trees same return true
        if self.sameTree(root,subRoot):
            return True


        # recursive call to isSubtree instead of sameTree
        return (self.isSubtree(root.left, subRoot) or
        self.isSubtree(root.right, subRoot))


    def sameTree(self, s, t):
        if not s and not t:
            return True

        if s and t and s.val == t.val:
            # compare rest of subtree left and right
            return (self.sameTree(s.left, t.left) and
            self.sameTree(s.right, t.right))

        return False
