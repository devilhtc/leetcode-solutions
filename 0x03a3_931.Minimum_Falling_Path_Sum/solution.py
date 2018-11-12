class Solution(object):
    def minFallingPathSum(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        m, n = len(A), len(A[0])
        dp = [[0] * n for _ in range(m)]
        for j in range(n):
            dp[0][j] = A[0][j]

        for i in range(1, m):
            for j in range(n):
                dp[i][j] = dp[i - 1][j]
                if j > 0:
                    dp[i][j] = min(dp[i][j], dp[i - 1][j - 1])
                if j < n - 1:
                    dp[i][j] = min(dp[i][j], dp[i - 1][j + 1])
                dp[i][j] += A[i][j]
        return min(dp[-1])
