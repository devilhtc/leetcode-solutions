class RQ:
    def __init__(self, lo, hi, amount=1):
        self.lo = lo
        self.hi = hi
        self.children = []
        self.cur = amount
        self.max = amount

    def query(self, start, end):
        if (start <= self.lo and end >= self.hi) or len(self.children) == 0:
            return self.max
        if start < self.lo:
            start = self.lo
        if end > self.hi:
            end = self.hi

        s_idx, e_idx = self._q(start, end)

        i = s_idx
        out = self.max
        while i < e_idx + 1:
            out = max(
                out, self.children[i].query(
                    start,
                    end
                )
            )
        return out
        
    def add(self, start, end, amount=1):
        if start <= self.lo and end >= self.hi:
            self.cur += amount
            self.max += amount
            for c in self.children:
                c.add(start, end, amount)
            self._rf()
            return

        if start < self.lo:
            start = self.lo
        if end > self.hi:
            end = self.hi

        s_idx, e_idx = self._q(start, end)
        new_amount = amount + self.cur
        if s_idx == -1: # empty children, or < all
            newc = RQ(start, end, amount=new_amount)
            self.children = [newc] + self.children
            self.max = max(newc.max, self.max)
            self._rf()
            return

        if s_idx == 0 and e_idx == -1: # no overlap, > all
            newc = RQ(start, end, amount=new_amount)
            self.children.append(newc)
            self.max = max(newc.max, self.max)
            self._rf()
            return
        
        new_children = []
        p = start

        for i, c in enumerate(self.children):
            if i < s_idx or i > e_idx:
                new_children.append(c)
                continue
            if p < c.lo:
                newc = RQ(p, c.lo, amount=new_amount)
                self.max = max(self.max, newc.amount)
                new_children.append(newc)
                p = c.end
            new_children.append(c)
            c.add(start, end, amount)
            if i == e_idx and end > c.hi:
                newc = RQ(c.hi, end, amount=new_amount)
                self.max = max(self.max, newc.amount)
                new_children.append(newc)
        
        self._rf()
        return
        
    def _rf(self):
        if len(self.children) > 5:
            print('need rf')
        pass

    def _q(self, start, end):
        if len(self.children) == 0:
            return -1, -1
        if self.children[0].lo > end:
            return -1, 0
        if self.children[-1].hi < start:
            return 0, -1

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
                hi = mi - 1
            else:
                lo = mi
        e_idx = lo

        return s_idx, e_idx
    
def main():
    a = RQ(0, 10)
    print('a.query(0, 10)', a.query(0, 10))
    print('a.query(0, 3)', a.query(0, 3))
    print('a.add(1, 2)', a.add(1, 2))
    print('a.add(1, 2)', a.add(1, 2))
    print('a.query(1, 2)', a.query(1, 2))

if __name__ == '__main__':
    main()