class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        n = len(graph)
        labels = {}
        ret = {0: True}

        def dfs(i, l):
            if i not in labels:
                labels[i] = l
                for j in graph[i]:
                    dfs(j, -l)
            else:
                if labels[i] == l:
                    return
                else:
                    ret[0] = False

        for i in range(n):
            if i not in labels:
                dfs(i, 1)
        return ret[0]
