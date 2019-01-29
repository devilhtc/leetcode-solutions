class Solution:
    def mincostToHireWorkers(self, quality, wage, K):
        """
        :type quality: List[int]
        :type wage: List[int]
        :type K: int
        :rtype: float
        """
        wpq_q = sorted([(wage[i] / quality[i], quality[i]) for i in range(len(wage))])
        qualities = []
        total_q = 0
        for i in range(K - 1):
            heapq.heappush(qualities, -wpq_q[i][1])
            total_q += wpq_q[i][1]
        out = float("inf")
        for i in range(K - 1, len(wage)):
            wpq, q = wpq_q[i]
            out = min(wpq * (q + total_q), out)
            heapq.heappush(qualities, -q)
            popped = -heapq.heappop(qualities)
            total_q = total_q + q - popped
        return out
