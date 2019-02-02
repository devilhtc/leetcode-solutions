class Solution:
    def __init__(self, N, blacklist):
        """
        :type N: int
        :type blacklist: List[int]
        """
        blacklist.append(N)
        blacklist = sorted(blacklist)
        self.n = N - len(blacklist) + 1
        self.ranges = []
        arr = []
        p = 0
        for b in blacklist:
            if b - 1 >= p:
                arr.append((p, b - 1))
            p = b + 1
        i = 0
        for s, e in arr:
            self.ranges.append((i, i + e - s, s - i))
            i += e - s + 1

    def pick(self):
        """
        :rtype: int
        """
        k = random.randint(0, self.n - 1)
        lo = 0
        hi = len(self.ranges) - 1
        if self.ranges[lo][1] >= k >= self.ranges[lo][0]:
            return k + self.ranges[lo][2]
        elif self.ranges[hi][1] >= k >= self.ranges[hi][0]:
            return k + self.ranges[hi][2]
        while hi > lo:
            mi = (hi + lo) // 2
            if self.ranges[mi][1] >= k >= self.ranges[mi][0]:
                return k + self.ranges[mi][2]
            elif k < self.ranges[mi][0]:
                hi = mi - 1
            else:
                lo = mi + 1
        return k + self.ranges[lo][2]


# Your Solution object will be instantiated and called as such:
# obj = Solution(N, blacklist)
# param_1 = obj.pick()
