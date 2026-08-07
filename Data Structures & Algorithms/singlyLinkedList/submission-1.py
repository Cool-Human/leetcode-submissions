class ListNode:
    def __init__(self, val = 0, nxt = None):
        self.val = val
        self.nxt = nxt

class LinkedList:
    
    def __init__(self):
        self.head = ListNode(-1)
        self.tail = self.head
    
    def get(self, index: int) -> int:
        curr = self.head.nxt
        i = 0
        while curr:
            if i == index:
                return curr.val
            i += 1
            curr = curr.nxt
        return -1

    def insertHead(self, val: int) -> None:
        new_start_node = ListNode(val)
        new_start_node.nxt = self.head.nxt
        self.head.nxt = new_start_node
        if not new_start_node.nxt:
            self.tail = new_start_node

    def insertTail(self, val: int) -> None:
        self.tail.nxt = ListNode(val)
        self.tail = self.tail.nxt

    def remove(self, index: int) -> bool:
        i = 0
        curr = self.head
        while i < index and curr:
            i += 1
            curr = curr.nxt
        
        if curr and curr.nxt:
            if curr.nxt == self.tail:
                self.tail = curr
            curr.nxt = curr.nxt.nxt
            return True
        return False

    def getValues(self) -> List[int]:
        curr = self.head.nxt
        res =[]
        while curr:
            res.append(curr.val)
            curr = curr.nxt
        return res
