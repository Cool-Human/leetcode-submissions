class ListNode:

    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.head = ListNode()
        self.size = 0

    def get(self, index: int) -> int:
        if index + 1 <= self.size:
            curr = self.head
            for _ in range(index + 1):
                curr = curr.next
            return curr.val
        return -1

    def addAtHead(self, val: int) -> None:
        temp = ListNode(val, self.head.next)
        self.head.next = temp
        self.size += 1
        return

    def addAtTail(self, val: int) -> None:
        temp = ListNode(val)
        curr = self.head
        for _ in range(self.size):
            curr = curr.next
        curr.next = temp
        self.size += 1
        return

    def addAtIndex(self, index: int, val: int) -> None:
        if index <= self.size:
            curr = self.head
            for _ in range(index):
                curr = curr.next
            temp = ListNode(val, curr.next)
            curr.next = temp
            self.size += 1
            return

    def deleteAtIndex(self, index: int) -> None:
        if 0 <= index < self.size:
            curr = self.head
            for _ in range(index):
                curr = curr.next
            curr.next = curr.next.next
            self.size -= 1
            return
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)