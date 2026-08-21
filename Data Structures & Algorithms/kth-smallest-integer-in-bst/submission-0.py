class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # number of elements we have visited
        # once n =k then we have our answer
        # inorder iteratively
        n = 0

        stack = []

        # what node we are currently at
        curr=root

        # while current node is not null or stack is not empty
        while curr or stack:
            while curr:
                # we have  to go back to current node after we are done processing left tree of current so we just add current node to stack to come back to it laater
                stack.append(curr)
                # keep going left - go to every node in left subtree before we visit the current ndoe
                curr = curr.left

            # when while loop is done executing curr is at null
            # pop last element 
            curr = stack.pop()
            n+=1
            if n==k:
                return curr.val
            # go to right subtree
            curr = curr.right