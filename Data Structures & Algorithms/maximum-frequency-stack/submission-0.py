class FreqStack:

    def __init__(self):
        self.stack = []
        self.idx = 0
        self.counter = defaultdict(int)

    def push(self, val: int) -> None:
        self.counter[val] += 1
        heapq.heappush_max(self.stack, (self.counter[val], self.idx, val))
        self.idx += 1

    def pop(self) -> int:
        _, _, val = heapq.heappop_max(self.stack)
        self.counter[val] -= 1
        return val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()