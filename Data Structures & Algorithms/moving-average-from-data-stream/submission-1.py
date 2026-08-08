from collections import deque

class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.window = deque()
        self.window_sum = 0

    def next(self, val: int) -> float:
        if len(self.window) == self.size:
            self.window_sum -= self.window.popleft()
        
        self.window.append(val)
        self.window_sum += val

        return self.window_sum / len(self.window)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
