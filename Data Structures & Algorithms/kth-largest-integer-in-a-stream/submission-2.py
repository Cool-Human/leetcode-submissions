import bisect

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        nums.sort(reverse=True)
        self.stack = nums[:k]
        self.length = k

    def add(self, val: int) -> int:
        bisect.insort(self.stack, val, key = lambda x: -x)
        while len(self.stack) > self.length:
            self.stack.pop()
        return self.stack[-1]