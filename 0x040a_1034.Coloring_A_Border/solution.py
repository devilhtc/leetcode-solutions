class Solution:
    def colorBorder(
        self, grid: List[List[int]], r0: int, c0: int, color: int
    ) -> List[List[int]]:
        m = len(grid)
        if m == 0:
            return grid
        n = len(grid[0])
        dij = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        visited = set()
        tocolor = []

        def inbound(i, j):
            return 0 <= i < m and 0 <= j < n

        def dfs(i, j, v):
            if grid[i][j] != v:
                return
            if (i, j) in visited:
                return
            visited.add((i, j))
            isborder = False
            for di, dj in dij:
                i2, j2 = i + di, j + dj
                if not inbound(i2, j2) or abs(grid[i2][j2]) != v:
                    isborder = True
                else:
                    dfs(i2, j2, v)
            if isborder:
                tocolor.append((i, j))

        dfs(r0, c0, grid[r0][c0])
        for i, j in tocolor:
            grid[i][j] = color
        return grid
