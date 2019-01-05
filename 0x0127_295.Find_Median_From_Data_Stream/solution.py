class MedianFinder:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.lo = []
        self.hi = []
        self.mi = None
        self.size = 0

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        if self.size == 0:
            self.mi = num
        elif self.size % 2 == 0:
            if -self.lo[0] <= num <= self.hi[0]:
                self.mi = num
            elif num < -self.lo[0]:
                self.mi = -heapq.heappop(self.lo)
                heapq.heappush(self.lo, -num)
            else:
                self.mi = heapq.heappop(self.hi)
                heapq.heappush(self.hi, num)
        else:
            if num <= self.mi:
                heapq.heappush(self.lo, -num)
                heapq.heappush(self.hi, self.mi)
            else:
                heapq.heappush(self.hi, num)
                heapq.heappush(self.lo, -self.mi)
            self.mi = None
        self.size += 1

    def findMedian(self):
        """
        :rtype: float
        """
        # print(self.lo, self.hi, self.mi)
        if self.mi is not None:
            return self.mi * 1.0
        else:
            return (-self.lo[0] + self.hi[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
