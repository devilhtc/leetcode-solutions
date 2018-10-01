class Solution:
    def matrixScore(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        m, n = len(A), len(A[0])
        out = m
        for i in range(1, n):
            ones = sum(A[j][i] ^ A[j][0] for j in range(m))
            out = out * 2 + max(ones, m - ones)
        return out
