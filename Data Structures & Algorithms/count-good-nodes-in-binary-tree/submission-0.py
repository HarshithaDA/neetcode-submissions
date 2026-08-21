# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
     # is max passed down greater than each node? - if no then its a good node else its a bad ndoe
    # recursive call for left and right subtree

        # counts the number of good nodes in left and right subtrees
        def dfs(node, maxVal):
            if not node:
                return 0

            # identify if this current node is a good node (res=1) or not (res=0)
            res = 1 if node.val >=maxVal else 0
            # update maxVal so far
            maxVal = max(maxVal, node.val)
            #counts the number of good nodes in left and right subtrees
            res += dfs(node.left, maxVal)
            res += dfs(node.right, maxVal)
            return res

        return dfs(root, root.val)


