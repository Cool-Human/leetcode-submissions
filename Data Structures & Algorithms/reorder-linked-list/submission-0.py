# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # for empty or single node linked lists
        if not head or not head.next:
            return
        
        # finding the middle most node and store it in variable-> 'slow'
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # reversing the second have of the list from 'slow' onwards
        prev, curr = None, slow.next
        slow.next = None # spliting the first half of the linked list from the second half

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        # 'prev' is the head of the later half of the original linked list that is now reversed

        # merging the 2 linked lists alternatively
        first, second = head, prev

        while second:
            a, b = first.next, second.next

            first.next, second.next = second, a

            first, second = a, b
        