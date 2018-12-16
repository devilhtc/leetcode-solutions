class RQ:
    def __init__(self, lo, hi, amount=1):
        self.lo = lo
        self.hi = hi
        self.children = []
        self.cur = amount
        self.max = amount

    def query(self, start, end):
        start = max(self.lo, start)
        end = min(self.hi, end)
        if (start == self.lo and end == self.hi) or len(self.children) == 0:
            return self.max

        out = self.cur
        for c in self.children:
            if c.hi > start and end > c.lo:
                out = max(out, c.query(start, end))

        self.max = max(self.max, out)
        return out

    def add(self, start, end, amount=1):
        start = max(self.lo, start)
        end = min(self.hi, end)

        if start == self.lo and end == self.hi:
            self.cur = amount + self.cur
            self.max = amount + self.max
            for c in self.children:
                c.add(start, end, amount)
            return

        new_amount = amount + self.cur
        self.max = max(new_amount, self.max)
        if len(self.children) == 0:
            self.children.append(RQ(start, end, amount=new_amount))
            self.max = max(self.max, new_amount)
            return

        unmapped = []
        s = start
        for i, c in enumerate(self.children):
            if s < c.lo and c.lo <= end:
                unmapped.append((s, c.lo))
                s = c.hi
            if self._ol((c.lo, c.hi), (start, end)):
                c.add(start, end, amount=amount)
                self.max = max(self.max, c.max)
                s = c.hi

        if s < end:
            unmapped.append((s, end))

        new_children = [RQ(i, j, amount=new_amount) for i, j in unmapped]
        self.children = sorted(self.children + new_children, key=lambda x: x.lo)
        self._rf()

    def _ol(self, itv1, itv2):
        return itv1[0] < itv2[1] and itv2[0] < itv1[1]

    def _rf(self):
        if len(self.children) > 5:

            mi = len(self.children) // 2
            b = self.children[mi - 1].hi

            leftc = []
            leftmax = self.cur
            rightc = []
            rightmax = self.cur

            for i, c in enumerate(self.children):
                if i < mi:
                    leftc.append(c)
                    leftmax = max(c.max, leftmax)
                else:
                    rightc.append(c)
                    rightmax = max(c.max, rightmax)

            left = RQ(self.lo, b, amount=self.cur)
            left.max = leftmax
            left.children = leftc
            right = RQ(b, self.hi, amount=self.cur)
            right.max = rightmax
            right.children = rightc

            self.children = [left, right]

    def _print(self, level=0):
        pl = lambda x: print("-" * level, *x)
        pl([self.lo, self.hi, self.cur])
        for c in self.children:
            c._print(level=level + 1)


class MyCalendarTwo:
    def __init__(self):
        self.rq = RQ(0, 10 ** 9, amount=0)

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        if self.rq.query(start, end) >= 2:
            return False
        self.rq.add(start, end)
        return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)
