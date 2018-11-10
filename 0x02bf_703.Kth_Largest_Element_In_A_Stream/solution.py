class KthLargest:
    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.pq = []
        self.k = k
        for n in nums:
            heapq.heappush(self.pq, n)
            if len(self.pq) > k:
                heapq.heappop(self.pq)

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        heapq.heappush(self.pq, val)
        if len(self.pq) > self.k:
            heapq.heappop(self.pq)
        return self.pq[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
