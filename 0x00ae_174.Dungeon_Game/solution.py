class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        m = len(dungeon)
        if m == 0:
            return 0
        n = len(dungeon[0])
        if n == 0:
            return 0
        memo = [[-1] * n for _ in range(m)]
        
        def dp(i, j):
            if memo[i][j] >= 0:
                return memo[i][j]
            if i == m - 1 and j == n - 1:
                out = max(1, 1 - dungeon[i][j])
            elif i == m - 1:
                a = dp(i, j + 1)
                out = max(1, a - dungeon[i][j])
            elif j == n - 1:
                b = dp(i + 1, j)
                out = max(1, b - dungeon[i][j])
            else:
                a = dp(i, j + 1)
                b = dp(i + 1, j)
                out = min(
                    max(1, a - dungeon[i][j]),
                    max(1, b - dungeon[i][j])
                )
            memo[i][j] = out
            return out
        
        out = dp(0, 0)
        return out