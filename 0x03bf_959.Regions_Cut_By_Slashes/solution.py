class Solution:
    def regionsBySlashes(self, grid):
        """
        :type grid: List[str]
        :rtype: int
        """
        uf = {}
        N = len(grid)

        def inbounds(i, j):
            return (0 <= i < N) and (0 <= j < N)

        def union(i, j):
            fi = find(i)
            fj = find(j)
            if fi == fj:
                return
            if fi > fj:
                fi, fj = fj, fi
            uf[fj] = fi

        def find(i):
            if i not in uf:
                uf[i] = i
            j = i
            while uf[j] != j:
                j = uf[j]
            uf[i] = j
            return j

        adj = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        for i in range(N):
            for j in range(N):
                base = i * N + j
                a = []
                for k in range(4):
                    di, dj = adj[k]
                    if inbounds(i + di, j + dj):
                        union(((i + di) * N + j + dj) * 4 + ((k + 2) % 4), base * 4 + k)
                if grid[i][j] != "/":
                    union(base * 4 + 0, base * 4 + 1)
                    union(base * 4 + 2, base * 4 + 3)
                if grid[i][j] != "\\":
                    union(base * 4 + 1, base * 4 + 2)
                    union(base * 4 + 0, base * 4 + 3)

        g = set()
        for i in range(N):
            for j in range(N):
                base = i * N + j
                for k in range(4):
                    g.add(find(base * 4 + k))

        return len(g)
