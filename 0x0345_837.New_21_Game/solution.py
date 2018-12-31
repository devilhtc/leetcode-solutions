class Solution:
    def new21Game(self, N, K, W):
        """
        :type N: int
        :type K: int
        :type W: int
        :rtype: float
        """
        if K == 0:
            return 1.0
        D = N - K
        dp = [0.0] * (K + W)
        c = 0.0
        for k in range(W):
            cur = 1.0 if k >= W + K - 1 - N else 0.0
            dp[k] = cur
            c += cur
        dp[W] = c / W
        for i in range(W + 1, K + W):
            dp[i] = dp[i - 1] + (dp[i - 1] - dp[i - 1 - W]) / W
        return dp[K + W - 1]
