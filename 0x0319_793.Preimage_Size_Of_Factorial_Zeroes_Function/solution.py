# solution by @awice O((logK)^2)

class Solution(object):
    def preimageSizeFZF(self, K):
        """
        :type K: int
        :rtype: int
        """
        def numZeros(x):
            if x == 0: return 0
            return x / 5 + numZeros(x / 5)
        
        lo, hi = K, 10 * K + 1
        while lo < hi:
            mi = (lo + hi) / 2
            n = numZeros(mi)
            if n == K: return 5
            if n < K:
                lo = mi + 1
            else:
                hi = mi
        return 0
        