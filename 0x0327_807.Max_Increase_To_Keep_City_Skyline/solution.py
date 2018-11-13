class Solution:
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        maxm = [0] * m
        maxn = [0] * n

        for i in range(m):
            for j in range(n):
                maxm[i] = max(maxm[i], grid[i][j])
                maxn[j] = max(maxn[j], grid[i][j])

        out = 0
        for i in range(m):
            for j in range(n):
                out += min(maxm[i], maxn[j]) - grid[i][j]
        return out
