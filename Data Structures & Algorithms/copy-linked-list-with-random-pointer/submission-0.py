"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # hash map - map old node to the copy of that node we create
        oldToCopy = {None:None}

        # iterate through linked list once
        curr = head
        # till current node becomes null ie reaches the end of the list
        # First loop pass
        while curr:
            # create copy of this node
            copy = Node(curr.val)
            # take this copy and put it in our hashmap
            oldToCopy[curr] = copy
            # update current pointer
            curr = curr.next

        curr = head
        # Second loop pass
        while curr:
            copy = oldToCopy[curr]
            # for this node we set the 2 pointers next and random
            copy.next = oldToCopy[curr.next]
            copy.random = oldToCopy[curr.random]
            curr = curr.next

        return oldToCopy[head]
