# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        curr = dummy

        length = 0
        while curr.next:
            curr = curr.next
            length += 1
        
        m = length - n

        if m < 0:
            return dummy.next
        
        curr = dummy
        while m > 0 and curr.next:
            curr = curr.next
            m -= 1
        
        if curr.next:
            curr.next = curr.next.next
        
        return dummy.next