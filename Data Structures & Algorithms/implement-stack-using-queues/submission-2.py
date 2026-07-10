from collections import deque

class MyStack:

    def __init__(self):
        self.stack = deque()

    def push(self, x: int) -> None:
        self.stack.appendleft(x)

    def pop(self) -> int:
        if self.stack:
            return self.stack.popleft()
        return None

    def top(self) -> int:
        if self.stack:
            return self.stack[0]
        return None

    def empty(self) -> bool:
        if self.stack:
            return False
        return True


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()