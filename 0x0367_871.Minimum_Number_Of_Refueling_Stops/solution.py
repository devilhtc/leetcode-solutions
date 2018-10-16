class Solution:
    def minRefuelStops(self, target, startFuel, stations):
        pq = []
        res = i = 0
        cur = startFuel
        while cur < target:
            while i < len(stations) and stations[i][0] <= cur:
                heapq.heappush(pq, -stations[i][1])
                i += 1
            if not pq:
                return -1
            cur += -heapq.heappop(pq)
            res += 1
        return res
