# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        stack = set()
        pointer = head
        while pointer:
            if pointer in stack:
                return True
            stack.add(pointer)
            pointer = pointer.next
        return False