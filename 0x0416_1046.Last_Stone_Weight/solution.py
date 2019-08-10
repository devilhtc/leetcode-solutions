class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        pq = []
        for s in stones:
            heapq.heappush(pq, -s)

        while len(pq) > 1:
            s1 = -heapq.heappop(pq)
            s2 = -heapq.heappop(pq)
            r = abs(s1 - s2)
            if r > 0:
                heapq.heappush(pq, -r)

        return 0 if len(pq) == 0 else -pq[0]
