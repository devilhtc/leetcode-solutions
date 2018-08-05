class Solution(object):
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        return (
            sum(1 for i in range(len(grid)) for j in range(len(grid)) if grid[i][j] > 0)
            + sum(max(v) for v in grid)
            + sum(max(v[i] for v in grid) for i in range(len(grid)))
        )
