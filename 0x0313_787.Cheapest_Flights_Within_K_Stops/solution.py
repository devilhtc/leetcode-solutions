class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """
        trips = K + 1
        dp = [[-1 for _ in range(n)] for _ in range(trips + 1)]
        dp[0][src] = 0
        out = -1
        for t in range(1, trips + 1):
            for e in flights:
                i = e[0]
                j = e[1]
                p = e[2]
                if dp[t - 1][i] >= 0:
                    cur_p = dp[t - 1][i] + p
                    dp[t][j] = cur_p if dp[t][j] == -1 else min(dp[t][j], cur_p)
            if dp[t][dst] >= 0:
                out = dp[t][dst] if out == -1 else min(out, dp[t][dst])
        # print dp
        return out
