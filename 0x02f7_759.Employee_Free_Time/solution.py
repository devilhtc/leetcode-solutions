# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e


class Solution:
    def employeeFreeTime(self, schedule: "List[List[Interval]]") -> "List[Interval]":
        n = len(schedule)
        pq = []
        for itvs in schedule:
            for itv in itvs:
                heapq.heappush(pq, (itv.start, 1))
                heapq.heappush(pq, (itv.end, -1))
        count = 0  # number of working employees
        prev = -1
        out = []
        while len(pq) > 0:
            t = pq[0][0]
            count2 = count
            while len(pq) > 0 and pq[0][0] == t:
                count2 += heapq.heappop(pq)[1]
            if count == 0 and count2 > 0 and prev != -1:
                out.append(Interval(prev, t))
            prev = t
            count = count2
        return out
