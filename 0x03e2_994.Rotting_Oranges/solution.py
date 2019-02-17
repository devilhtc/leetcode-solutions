class Solution:
    def orangesRotting(self, grid: "List[List[int]]") -> "int":
        m, n = len(grid), len(grid[0])
        q = collections.deque([])  # queue
        t = 0  # total number of oranges

        for i in range(m):
            for j in range(n):
                cell = grid[i][j]
                t += 1 if cell >= 1 else 0
                if cell == 2:
                    q.append((i, j, 0))

        dij = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        r = 0  # total number of rotten oranges
        last = 0  # last taken step

        # BFS
        while len(q) > 0:
            i, j, s = q.popleft()
            r += 1
            last = s

            # propagate to fresh neighbors
            for di, dj in dij:
                i2 = i + di
                j2 = j + dj
                if not (0 <= i2 < m and 0 <= j2 < n):
                    continue  # out of bounds
                if grid[i2][j2] == 1:
                    grid[i2][j2] = 2
                    q.append((i2, j2, s + 1))

        if r == t:
            return last
        return -1
