class Solution:
    def numEnclaves(self, A: List[List[int]]) -> int:
        uf = {-1: -1}
        m, n = len(A), len(A[0])

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

        def ij2k(i, j):
            return i * n + j

        total = 0

        for i in range(m):
            for j in range(n):
                if A[i][j] == 0:
                    continue
                if i == 0 or j == 0 or i == m - 1 or j == n - 1:
                    union(ij2k(i, j), -1)
                total += 1
                for di, dj in [(0, -1), (-1, 0)]:
                    i2, j2 = i + di, j + dj
                    if i2 >= 0 and j2 >= 0 and A[i2][j2] == 1:
                        union(ij2k(i, j), ij2k(i2, j2))

        walkoff = sum(1 for k in uf if find(k) == -1) - 1
        return total - walkoff
