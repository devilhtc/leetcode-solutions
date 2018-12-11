class RQ:
    def __init__(self, lo, hi):
        self.lo = lo
        self.hi = hi
        self.children = []
        self.cur = 1
        self.max = 1

    def query(self, start, end):
        if (start <= self.lo and end >= self.hi) or len(self.children) == 0:
            return self.max
        if start < self.lo:
            start = self.lo
        if end > self.hi:
            end = self.hi

        s_idx = e_idx = -1

        lo, hi = 0, len(self.children) - 1
        while hi > lo:
            mi = (hi + lo) // 2
            if self.children[mi].hi < start:
                lo = mi + 1
            else:
                hi = mi
        
        s_idx = lo

        lo, hi = 0, len(self.children) - 1
        while hi > lo:
            mi = (hi + lo) // 2
            if self.children[mi].lo > end:
                hi = mi
            else:
                lo = mi
        
        e_idx = lo
        
    def add(self, start, end):
        pass
