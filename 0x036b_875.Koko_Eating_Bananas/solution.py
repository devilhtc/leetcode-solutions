class Solution:
    def minEatingSpeed(self, piles, H):
        """
        :type piles: List[int]
        :type H: int
        :rtype: int
        """
        lo = 1
        hi = max(piles)
        while lo < hi:
            mi = (lo + hi) // 2
            x = sum((p - 1) // mi + 1 for p in piles)
            if x > H:
                lo = mi + 1
            elif x <= H:
                hi = mi
        return lo
