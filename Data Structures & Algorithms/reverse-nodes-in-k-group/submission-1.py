# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        next_group = head
        length = k

        while length and next_group:
            next_group = next_group.next
            length -= 1
        
        if length != 0:
            return head
        
        curr = head
        prev = self.reverseKGroup(next_group, k)

        while curr != next_group:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        return prev
