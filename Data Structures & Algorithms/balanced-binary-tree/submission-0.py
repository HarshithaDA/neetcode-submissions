# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        

        def dfs(root):
            # empty tree is just balanced # (isbalanced, height)
            if not root: return [True,0]

            # check if from the left subtree is it balanced and from the right subtree is it balanced?
            left, right = dfs(root.left), dfs(root.right)

            # from root node is it balanced?
            # get absolute value from left and right heights -> this balance has to be less than 1
            # make sure left and right are balanced and they are not null/false
            balance = (left[0] and right[0] and abs(left[1]- right[1])<=1)



            return [balance, 1+max(left[1], right[1])]

        return dfs(root)[0]
