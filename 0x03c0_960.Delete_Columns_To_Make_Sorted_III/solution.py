class Solution:
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        m, n = len(A), len(A[0])
        dp = [1] * n
        for i in range(1, n):
            for j in range(i):
                if all(A[k][i] >= A[k][j] for k in range(m)):
                    dp[i] = max(dp[i], dp[j] + 1)
        return n - max(dp)
