class MovingAverage:

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.dq = collections.deque()
        self.rs = 0
        self.size = 0
        self.limit = size

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        self.dq.append(val)
        self.rs += val
        self.size += 1
        if self.size > self.limit:
            a = self.dq.popleft()
            self.rs -= a
            self.size -= 1
        return self.rs / self.size
            
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)