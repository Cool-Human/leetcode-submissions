class ListNode:
    def __init__(self, val: float, prv: Optional['ListNode'] = None, nxt: Optional['ListNode'] = None) -> None:
        self.val = val
        self.nxt = nxt
        self.prv = prv

class MedianFinder:

    def __init__(self):
        self.size = 0
        self.head = ListNode(float('-inf'))
        self.tail = ListNode(float('+inf'), self.head)
        self.head.nxt = self.tail

    def addNum(self, num: int) -> None:

        def position(node, value):
            while node.val < value:
                node = node.nxt
            return node.prv
        
        node = position(self.head, num)
        tmp = node.nxt
        x = ListNode(num, node, tmp)
        node.nxt = tmp.prv = x
        self.size += 1

    def findMedian(self) -> float:
        if not self.size:
            return 0
        
        def index(node, iterator):
            while iterator:
                node = node.nxt
                iterator -= 1
            return node
        
        idx = (self.size + 1) // 2
        if self.size % 2 == 0:
            node = index(self.head, idx)
            return (node.val + node.nxt.val) / 2
        else:
            node = index(self.head, idx)
            return float(node.val)