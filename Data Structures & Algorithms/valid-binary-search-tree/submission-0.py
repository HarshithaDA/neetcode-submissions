# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # left boundary and right boundary
        

        def valid(node, left, right):
            # an empty binary search tree is valid
            if not node:
                return True

            # found a node that broke the left and right boundary condition - not a valid BST
            if not (node.val<right and node.val>left):
                return False

            # recursive call
            # make sure left subtree of node is valid BST also
            # boundary will be the left boundary and update the right boundary to the node's value
            # every value in the left of left subtree has to be less than the parent 
            return (valid(node.left, left, node.val) and
            valid(node.right, node.val, right))

        return valid(root, float("-inf"), float("inf"))
