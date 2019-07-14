class Solution:
    def minScoreTriangulation(self, A: List[int]) -> int:
        memo = {}

        def dp(i, j):
            if j - i == 1:
                return 0
            if j - i == 2:
                return A[i] * A[i + 1] * A[i + 2]
            if (i, j) in memo:
                return memo[(i, j)]
            minScore = float("inf")
            for k in range(i + 1, j):
                score = A[i] * A[j] * A[k] + dp(i, k) + dp(k, j)
                minScore = min(minScore, score)
            memo[(i, j)] = minScore
            return minScore

        return dp(0, len(A) - 1)
