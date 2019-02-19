class Solution:
    def pacificAtlantic(self, matrix: "List[List[int]]") -> "List[List[int]]":
        m, n = len(matrix), len(matrix[0]) if len(matrix) > 0 else 0
        if m == 0 or n == 0:
            return []
        dij = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(i, j, visited):
            if (i, j) in visited:
                return
            visited.add((i, j))
            for di, dj in dij:
                i2, j2 = i + di, j + dj
                if not (0 <= i2 < m and 0 <= j2 < n):
                    continue
                if matrix[i2][j2] >= matrix[i][j]:
                    dfs(i2, j2, visited)

        def find(starts):
            visited = set()
            for i, j in starts:
                dfs(i, j, visited)
            return visited

        def convert(l):
            return [list(ele) for ele in l]

        pstarts = [(0, 0)]
        astarts = [(m - 1, n - 1)]
        for i in range(m - 1):
            pstarts.append((i + 1, 0))
            astarts.append((i, n - 1))
        for j in range(n - 1):
            pstarts.append((0, j + 1))
            astarts.append((m - 1, j))

        return convert(sorted(list(find(pstarts) & find(astarts))))
