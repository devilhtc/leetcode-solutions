class Solution(object):
    def largestSumOfAverages(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: float
        """
        Acum = [0.0]
        dp = [[0.0 for _ in range(len(A))] for _ in range(K)]
        for a in A:
            Acum.append(Acum[-1] + a)
        for j in range(len(A)):
            dp[0][j] = Acum[j + 1] / (j + 1)
        for i in range(1, K):
            for j in range(i, len(A)):
                dp[i][j] = max(
                    dp[i - 1][k] + (Acum[j + 1] - Acum[k + 1]) / (j - k)
                    for k in range(i - 1, j)
                )
        return dp[-1][-1]
