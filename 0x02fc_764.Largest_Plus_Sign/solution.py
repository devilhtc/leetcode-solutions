class Solution(object):
    def orderOfLargestPlusSign(self, N, mines):
        """
        :type N: int
        :type mines: List[List[int]]
        :rtype: int
        """
        grid = [[1] * N for _ in range(N)]
        l = [[1] * N for _ in range(N)]
        r = [[1] * N for _ in range(N)]
        u = [[1] * N for _ in range(N)]
        d = [[1] * N for _ in range(N)]
        for m in mines:
            i, j = m[0], m[1]
            grid[i][j] = 0
            l[i][j] = 0
            r[i][j] = 0
            u[i][j] = 0
            d[i][j] = 0
        for i in range(1, N):
            for j in range(1, N):
                l[i][j] = grid[i][j] * (l[i - 1][j] + 1)
                u[i][j] = grid[i][j] * (u[i][j - 1] + 1)
                ii = N - i - 1
                jj = N - j - 1
                r[ii][jj] = grid[ii][jj] * (r[ii + 1][jj] + 1)
                d[ii][jj] = grid[ii][jj] * (d[ii][jj + 1] + 1)
        out = 0
        for i in range(N):
            for j in range(N):
                out = max(out, min([l[i][j], r[i][j], u[i][j], d[i][j]]))
        return out
            
            
        