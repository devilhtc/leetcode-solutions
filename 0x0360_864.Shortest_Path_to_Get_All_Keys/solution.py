class Solution:
    def shortestPathAllKeys(self, grid):
        """
        :type grid: List[str]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        deltas = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def ingrid(i, j):
            return 0 <= i < m and 0 <= j < n

        def c2i(c):
            return ord(c.lower()) - ord("a")

        k = 0
        q = collections.deque([])
        dp = {}

        for i in range(m):
            for j in range(n):
                c = grid[i][j]
                if c == "@":
                    q.append(((i, j, 0), 0))
                    dp[(i, j, 0)] = 0
                elif c != "." and c != "#":
                    k = max(k, c2i(c) + 1)

        des = 2 ** k - 1

        while len(q) > 0:
            key, step = q.popleft()
            i, j, sig = key
            for di, dj in deltas:
                i2, j2 = i + di, j + dj
                if not ingrid(i2, j2):
                    continue
                p = grid[i2][j2]
                if p == "#":
                    continue
                if p == "." or p == "@":
                    sig2 = sig
                elif p == p.lower():
                    sig2 = sig | (1 << c2i(p))
                    if sig2 == des:
                        return step + 1
                elif p == p.upper():
                    if sig & (1 << c2i(p)) == 0:
                        continue
                    sig2 = sig
                key2 = (i2, j2, sig2)
                if key2 in dp:
                    continue
                dp[key2] = step + 1
                q.append((key2, step + 1))

        return -1
