class StockSpanner(object):
    def __init__(self):
        self.stack = []
        self.i = 1

    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        item = (price, self.i)
        self.i = self.i + 1

        while len(self.stack) > 0 and self.stack[-1][0] <= price:
            self.stack.pop()

        self.stack.append(item)

        if len(self.stack) == 1:
            return item[1]
        else:
            return item[1] - self.stack[-2][1]


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
