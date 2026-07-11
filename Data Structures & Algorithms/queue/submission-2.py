class Node:
    def __init__(self, val = -1, prev = None, next = None):
        self.val = val
        self.prev = prev
        self.next = next

class Deque:
    
    def __init__(self):
        self.head = Node(-1)
        self.tail = Node(-1)

        self.head.next = self.tail
        self.tail.prev = self.head
        return

    def isEmpty(self) -> bool:
        return self.head.next == self.tail

    def append(self, value: int) -> None:
        prev_node = self.tail.prev
        new_node = Node(value, prev_node, self.tail)
        self.tail.prev = new_node
        prev_node.next = new_node
        return

    def appendleft(self, value: int) -> None:
        next_node = self.head.next
        new_node = Node(value, self.head, next_node)
        self.head.next = new_node
        next_node.prev = new_node

    def pop(self) -> int:
        if not self.isEmpty():
            pop_node = self.tail.prev
            last_node = pop_node.prev
            last_node.next = self.tail
            self.tail.prev = last_node
            return pop_node.val
        else:
            return -1

    def popleft(self) -> int:
        if not self.isEmpty():
            pop_node = self.head.next
            first_node = pop_node.next
            first_node.prev = self.head
            self.head.next = first_node
            return pop_node.val
        else:
            return -1
