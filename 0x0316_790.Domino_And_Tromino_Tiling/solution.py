class Solution(object):
    def numTilings(self, N):
        """
        :type N: int
        :rtype: int
        """
        l = max(3, N + 1)

        MOD = 1000000007

        f = [0 for _ in range(l)]
        g = [0 for _ in range(l)]
        f[0] = 1
        f[1] = 1
        f[2] = 2
        g[2] = 1

        for i in range(3, l):
            f[i] = (2 * g[i - 1] + f[i - 1] + f[i - 2]) % MOD
            g[i] = (f[i - 2] + g[i - 1]) % MOD

        return f[N]
