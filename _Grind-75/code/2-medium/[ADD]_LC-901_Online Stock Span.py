# https://leetcode.com/problems/online-stock-span/

class StockSpanner:
    """
    price
    span

    100 80  60
    1   1   1

    100 80  70
    1   1   (1)+1

    100 80  70  60
    1   1   2   1

    100 80  75
    1   1   (2+1)+1

    100 85
    1   (1+4)+1
    """

    def __init__(self):
        # decreasing monotonic stack
        self.stack = []  # [(stock, span)]

    def next(self, price: int) -> int:
        span = 1
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack.pop()[1]
        self.stack.append((price, span))

        return span

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
