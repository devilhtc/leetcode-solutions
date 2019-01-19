class Solution:
    def swimInWater(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        if grid[-1][-1] == n ** 2 - 1:
            return n ** 2 - 1

        uf = {}

        def find(i):
            if i not in uf:
                uf[i] = i
                return i

            o = i
            while uf[i] != i:
                i = uf[i]
            uf[o] = i
            return i

        def union(i, j):
            fi = find(i)
            fj = find(j)
            if fi == fj:
                return

            if fi < fj:
                uf[fj] = fi
            else:
                uf[fi] = fj

        e2k = {}
        for i in range(n):
            for j in range(n):
                e2k[grid[i][j]] = i * n + j
        deltas = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for w in range(n ** 2):
            k = e2k[w]
            i, j = divmod(k, n)
            for di, dj in deltas:
                i2, j2 = i + di, j + dj
                if 0 <= i2 < n and 0 <= j2 < n:
                    if grid[i2][j2] <= w:
                        union(k, i2 * n + j2)
            if find(0) == find(n ** 2 - 1):
                return w
        return n ** 2 - 1
