class Solution:
    def surfaceArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        out = 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                out += (
                    0
                    if grid[i][j] == 0
                    else (
                        2
                        + sum(
                            max(
                                0,
                                grid[i][j]
                                - (
                                    grid[ii][jj] if (0 <= ii < m and 0 <= jj < n) else 0
                                ),
                            )
                            for ii, jj in [
                                (i - 1, j),
                                (i + 1, j),
                                (i, j - 1),
                                (i, j + 1),
                            ]
                        )
                    )
                )
        return out
