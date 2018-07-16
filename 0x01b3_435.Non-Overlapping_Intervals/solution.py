# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e


class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        # if empty, return 0
        l = len(intervals)
        if l == 0:
            return 0

        # sort the intervals by end and then start
        def cmp_itv(a, b):
            if a.end == b.end:
                return a.start - b.start
            else:
                return a.end - b.end

        itvs = sorted(intervals, cmp=cmp_itv)

        # conduct longest increasing subsequence
        keeps = [0 for _ in range(l)]
        prevmaxs = [0 for _ in range(l)]
        prevmax = 1
        for i in range(l):
            itv = itvs[i]
            lo, hi = 0, i
            # binary search
            while lo < hi - 1:
                mi = (lo + hi) / 2
                if itvs[mi].end > itv.start:
                    hi = mi
                else:
                    lo = mi
            keeps[i] = 1 if itv.start < itvs[0].end else prevmaxs[lo] + 1
            prevmaxs[i] = max(prevmax, keeps[i])
            prevmax = prevmaxs[i]
        return l - max(keeps)
