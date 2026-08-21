# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # base case no nodes return null
        if not preorder or not inorder:
            return None

        # first val in preorder list is always root node
        root = TreeNode(preorder[0])
        # find posiition of it in the inorder array
        mid = inorder.index(preorder[0])

        # start from 1 cuz we already created a node for index 0 - rott
        # from index 1 to mid
        # from beginning to mid not including mid
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])

        return root