# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # next pointer of thsi node is set to the head of the list
        dummy = ListNode(0, head)
        left = dummy

        right = head
        while n>0 and right:
            right = right.next
            n-=1

        # until right reaches end of list
        while right:
            left = left.next
            right = right.next

        # delete that node
        left.next = left.next.next

        return dummy.next

