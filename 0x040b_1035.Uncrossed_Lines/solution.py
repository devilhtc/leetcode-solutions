class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        m = len(A)
        n = len(B)
        dp = [[None for _ in range(n + 1)] for _ in range(m + 1)]
        base = [0] * 4
        dp[0][0] = base
        for i in range(m):
            dp[i + 1][0] = base
        for j in range(n):
            dp[0][j + 1] = base
        for i in range(m):
            for j in range(n):
                x = max(dp[i][j])
                dp[i + 1][j + 1] = [
                    x,
                    max(dp[i + 1][j][1], dp[i + 1][j][3]),
                    max(dp[i][j + 1][2], dp[i][j + 1][3]),
                    (x + 1) if A[i] == B[j] else 0,
                ]
        return max(dp[-1][-1])
