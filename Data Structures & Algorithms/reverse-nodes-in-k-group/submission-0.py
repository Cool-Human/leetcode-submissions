# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        next_group = dummy.next
        length = k

        while length and next_group:
            next_group = next_group.next
            length -= 1
        
        if length != 0:
            return dummy.next
        
        curr = dummy.next
        prev = self.reverseKGroup(next_group, k)

        while curr != next_group:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        return prev
