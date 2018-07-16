class Solution(object):
    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        n = len(graph)
        counts = {i: len(graph[i]) for i in range(n)}
        incoming = {i: [] for i in range(n)}
        for i in range(n):
            for j in graph[i]:
                incoming[j].append(i)

        def dfs(i):
            counts[i] = counts[i] - 1
            if counts[i] == 0:
                for j in incoming[i]:
                    dfs(j)

        seeds = [i for i in range(n) if counts[i] == 0]
        for s in seeds:
            for c in incoming[s]:
                dfs(c)

        out = [i for i in range(n) if counts[i] == 0]
        return out
