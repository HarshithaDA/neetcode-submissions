# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # we want to reverse the linked list only from the left position to the right position
        # first node from left position, break that link and set to null
        # next position break the next link and set to prev
        # so on
        # left most node now has to point to the node after the rightmost node
        # right most node now has to point to the first node

        # what ever dummy node points to is the head
        # phase 1: get a pointer to reach the left position node
        # phase 2: prev pointer has to point to node before that

        # dummy node points to head
        # prev ptr at dummy node, cur ptr at head node
        # cur node has to iterate (l-1) times before cur ptr will point to left node
        # create dummy node with value 0 that points to head node
        dummy = ListNode(0,head)
        leftprev, cur = dummy, head

        # reach left node
        for i in range(left-1):
            leftprev, cur = cur, cur.next

        # cur node is pointing to left ndoe, leftprev pointing to node before left
        # reverse sublist
        prev  = None
        for i in range(right-left+1):
            tempnext = cur.next
            cur.next = prev
            prev, cur = cur, tempnext

        # leftprev.next.next set to curr node
        # leftprev.next set to prev
        leftprev.next.next = cur
        leftprev.next = prev

        return dummy.next