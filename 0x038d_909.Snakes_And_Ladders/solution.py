class Solution:
    def smallestRangeII(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        if len(A) == 0:
            return 0
        A = sorted(A)
        r = A[-1] - A[0]
        for i in range(len(A) - 1):
            curmin = min(A[0] + K, A[i+1] - K)
            curmax = max(A[-1] - K, A[i] + K)
            if curmax - curmin < r:
                r = curmax - curmin
        return r

