class Solution:
    def numsSameConsecDiff(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: List[int]
        """
        if N == 1:
            return list(range(10))

        dp = [[[] for _ in range(10)] for _ in range(N)]
        dp[0] = [[i] for i in range(10)]
        for i in range(1, N):
            for j in range(10):
                for k in set([j - K, j + K]):
                    if not 0 <= k < 10:
                        continue
                    for n in dp[i - 1][k]:
                        dp[i][j].append(j * 10 ** i + n)

        out = []
        for j in range(1, 10):
            for n in dp[N - 1][j]:
                out.append(n)
        return out
