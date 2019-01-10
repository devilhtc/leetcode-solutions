# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e


class Solution:
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        pq = []
        for itv in sorted(intervals, key=lambda x: x.start):
            if len(pq) == 0:
                heapq.heappush(pq, itv.end)
            else:
                if pq[0] <= itv.start:
                    heapq.heappop(pq)
                heapq.heappush(pq, itv.end)
        return len(pq)
