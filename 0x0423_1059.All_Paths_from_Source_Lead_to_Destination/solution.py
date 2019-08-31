class Solution:
    def leadsToDestination(
        self, n: int, edges: List[List[int]], source: int, destination: int
    ) -> bool:
        g = collections.defaultdict(list)
        for f, t in edges:
            g[f].append(t)
        visited = collections.defaultdict(bool)
        if len(g[destination]) > 0:
            return False
        hasLoop = [False]
        reached = [False]
        reachedOthers = [False]

        def dfs(i):
            if hasLoop[0] == True:
                return
            if visited[i]:
                hasLoop[0] = True
                return
            if i == destination:
                reached[0] = True
            if len(g[i]) == 0 and i != destination:
                reachedOthers[0] = True
            visited[i] = True
            for j in g[i]:
                dfs(j)
            visited[i] = False

        dfs(source)
        return reached[0] and not hasLoop[0] and not reachedOthers[0]
