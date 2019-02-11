class Solution:
    def __init__(self, rects: "List[List[int]]"):
        self.total = 0
        self.rects = []
        for r in rects:
            x1, y1, x2, y2 = r
            numpoints = (x2 - x1 + 1) * (y2 - y1 + 1)
            self.rects.append((self.total + 1, self.total + numpoints, r))
            self.total += numpoints

    def pick(self) -> "List[int]":
        k = random.randint(1, self.total)
        lo = 0
        hi = len(self.rects) - 1
        while hi >= lo:
            mi = (hi + lo) // 2
            p, q, r = self.rects[mi]
            if k < p:
                hi = mi - 1
            elif k > q:
                lo = mi + 1
            else:
                x1, y1, x2, y2 = r
                return [random.randint(x1, x2), random.randint(y1, y2)]
        return None


# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()
