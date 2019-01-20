class Solution:
    def maxTurbulenceSize(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        d = [1] * len(A)
        u = [1] * len(A)
        for i, e in enumerate(A):
            if i == 0:
                continue
            if A[i] > A[i - 1]:
                u[i] = d[i - 1] + 1
            if A[i] < A[i - 1]:
                d[i] = u[i - 1] + 1
        return max([max(d), max(u)])
