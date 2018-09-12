class RLEIterator(object):
    def __init__(self, A):
        """
        :type A: List[int]
        """
        self.seq = list(A)
        self.cur = 0

    def next(self, n):
        """
        :type n: int
        :rtype: int
        """
        if self.cur >= len(self.seq):
            return -1
        elif self.seq[self.cur] >= n:
            self.seq[self.cur] -= n
            return self.seq[self.cur + 1]
        else:
            dec = self.seq[self.cur]
            self.cur = self.cur + 2
            return self.next(n - dec)


# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(A)
# param_1 = obj.next(n)
