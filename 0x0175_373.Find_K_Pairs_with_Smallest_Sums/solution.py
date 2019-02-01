class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        if len(nums1) == 0 or len(nums2) == 0:
            return []

        pq = []
        out = []
        inpq = set()
        heapq.heappush(pq, (nums1[0] + nums2[0], 0, 0))
        inpq.add((0, 0))
        for i in range(k):
            if len(pq) > 0:
                s, i, j = heapq.heappop(pq)
                out.append([nums1[i], nums2[j]])
                if i < len(nums1) - 1 and (i + 1, j) not in inpq:
                    heapq.heappush(pq, (nums1[i + 1] + nums2[j], i + 1, j))
                    inpq.add((i + 1, j))
                if j < len(nums2) - 1 and (i, j + 1) not in inpq:
                    heapq.heappush(pq, (nums1[i] + nums2[j + 1], i, j + 1))
                    inpq.add((i, j + 1))
        return out
