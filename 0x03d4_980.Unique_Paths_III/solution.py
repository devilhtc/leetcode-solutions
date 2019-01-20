class Solution:
    def uniquePathsIII(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])

        visited = [[False] * n for _ in range(m)]
        base = 0
        dessig = (1 << (m * n)) - 1
        dp = {}
        si, sj = 0, 0
        ei, ej = 0, 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == -1:
                    visited[i][j] = True
                    base = base | (1 << (i * n + j))
                if grid[i][j] == 1:
                    si = i
                    sj = j
                if grid[i][j] == 2:
                    ei = i
                    ej = j

        deltas = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def dfs(i, j, sig):
            if visited[i][j]:
                return 0
            cursig = sig | (1 << (i * n + j))
            if i == ei and j == ej:
                if cursig == dessig:
                    return 1
                else:
                    return 0
            if (cursig, i, j) in dp:
                return dp[(cursig, i, j)]

            visited[i][j] = True
            out = 0
            for di, dj in deltas:
                i2, j2 = i + di, j + dj
                if 0 <= i2 < m and 0 <= j2 < n:
                    out += dfs(i2, j2, cursig)
            dp[(cursig, i, j)] = out
            visited[i][j] = False
            return out

        o = dfs(si, sj, base)

        return o
