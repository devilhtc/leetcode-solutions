class Solution:
    def leastOpsExpressTarget(self, x, target):
        """
        :type x: int
        :type target: int
        :rtype: int
        """
        cost = list(range(40))
        cost[0] = 2
        memo = {}

        def dp(i, t):
            if t == 0:
                return 0
            if t == 1:
                return cost[i]
            if i >= 39:
                return target * 3
            if (i, t) in memo:
                return memo[(i, t)]
            nt, r = divmod(t, x)
            out = min(
                r * cost[i] + dp(i + 1, nt), (x - r) * cost[i] + dp(i + 1, nt + 1)
            )
            memo[(i, t)] = out
            return out

        return dp(0, target) - 1
