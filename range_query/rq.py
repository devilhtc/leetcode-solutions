import unittest
import random

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
                out = max(
                    out, c.query(start, end)
                )

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
            self.children.append(
                RQ(start, end, amount=new_amount)
            )
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
        
        new_children = [
            RQ(i, j, amount=new_amount) for i, j in unmapped
        ]
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
        pl = lambda x: print('-'*level, *x)
        pl([self.lo, self.hi, self.cur])
        for c in self.children:
            c._print(level=level+1)
    
class RQTestCase1(unittest.TestCase):
    def test_basic(self):
        a = RQ(3, 5)
        self.assertEqual(a.query(3,4), 1)

    def test_random(self):
        r = RQ(0, 1000)
        ranges = [
            (3, 5), (4, 7), (12, 100), (34, 54), (78, 124), (72, 185), (98, 900), (120, 130)
        ]
        track = [1] * 1000
        for _ in range(100):
            a = random.randint(2, 999)
            b = random.randint(2, 999)
            if a == b:
                continue
            a, b = min(a, b), max(a, b)
            r.add(a, b)
            for i in range(a, b):
                track[i] += 1
        r._print()
        for a, b in ranges:
            self.assertEqual(
                max(track[a: b]),
                r.query(a, b)
            )

if __name__ == '__main__':
    unittest.main()