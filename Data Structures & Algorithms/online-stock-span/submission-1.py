class StockSpanner:

    def __init__(self):
        self.prices = []

    def next(self, price: int) -> int:
        self.prices.append(price)
        max_count = 0
        count = 0
        for past_price in self.prices[::-1]:
            if past_price <= price:
                count += 1
            else:
                return count
        return count


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)