import random


class Solution:
    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.build(w)

    def build(self, w):
        self._w = [0.0]
        total = sum(w)
        cur = 0.0
        for i in w:
            cur += i
            self._w.append(cur / total)

    def pickIndex(self):
        """
        :rtype: int
        """
        return self._pickIndex(random.random())

    def _pickIndex(self, r):
        lo = 0
        hi = len(self._w) - 1
        while hi - lo > 1:
            mi = int((hi + lo) / 2)
            if r < self._w[mi]:
                hi = mi
            else:
                lo = mi
        return lo


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
