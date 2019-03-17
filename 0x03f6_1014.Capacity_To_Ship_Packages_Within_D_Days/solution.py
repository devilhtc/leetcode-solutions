from functools import lru_cache


class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        if len(weights) <= D:
            return max(weights)

        @lru_cache(maxsize=None)
        def days(cap):
            d = 1
            s = 0
            for w in weights:
                if w + s > cap:
                    d += 1
                    s = w
                else:
                    s = w + s
            return d

        lo = max(weights)
        hi = sum(weights)

        while hi > lo + 1:
            mi = (hi + lo) // 2
            d = days(mi)
            if d > D:
                lo = mi + 1
            else:
                hi = mi

        dl = days(lo)
        dh = days(hi)

        if dl <= D:
            return lo
        else:
            return hi
