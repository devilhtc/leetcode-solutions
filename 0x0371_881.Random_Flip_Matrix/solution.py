import random


class ReservoirSampling:
    def __init__(self, n):
        self.n = n
        self.build()

    def build(self):
        self.m = {}
        self.l = self.n

    def get_next(self):
        self.l = self.l - 1
        r = random.randint(0, self.l)
        self.m[r], self.m[self.l] = self.m.get(self.l, self.l), self.m.get(r, r)
        return self.m[self.l]

    def reset(self):
        self.build()


class Solution:
    def __init__(self, n_rows, n_cols):
        """
        :type n_rows: int
        :type n_cols: int
        """
        self.n_rows = n_rows
        self.n_cols = n_cols
        self.rs = ReservoirSampling(n_rows * n_cols)

    def flip(self):
        """
        :rtype: List[int]
        """
        n = self.rs.get_next()
        return self.n2rc(n)

    def n2rc(self, n):
        r = n // self.n_cols
        c = n - r * self.n_cols
        return [r, c]

    def reset(self):
        """
        :rtype: void
        """
        self.rs.reset()


# Your Solution object will be instantiated and called as such:
# obj = Solution(n_rows, n_cols)
# param_1 = obj.flip()
# obj.reset()
