class BrowserHistory:

    def __init__(self, homepage: str):
        self.store = []
        self.store.append(homepage)
        self.curr = 0
        return

    def visit(self, url: str) -> None:
        self.curr += 1
        self.store[self.curr:] = [url]
        return

    def back(self, steps: int) -> str:
        self.curr = max(0, self.curr - steps)
        return self.store[self.curr]

    def forward(self, steps: int) -> str:
        self.curr = min(len(self.store) - 1, self.curr + steps)
        return self.store[self.curr]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)