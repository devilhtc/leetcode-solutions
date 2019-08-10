class Solution:
    def gardenNoAdj(self, N: int, paths: List[List[int]]) -> List[int]:
        g = collections.defaultdict(list)
        for p in paths:
            g[p[0]].append(p[1])
            g[p[1]].append(p[0])
        color = [0] * N

        def dfs(i):
            if color[i - 1] != 0:
                return
            for c in range(1, 5):
                if any(color[j - 1] == c for j in g[i]):
                    continue
                color[i - 1] = c
                for j in g[i]:
                    dfs(j)

        for i in range(N):
            dfs(i)
        return color
