class Solution:
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if n <= 1:
            return k * n
        s = k
        d = k * (k - 1)
        for i in range(2, n):
            s, d = d, (d + s) * (k - 1)
        return s + d
        