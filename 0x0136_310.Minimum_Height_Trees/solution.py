class Solution:
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n == 1:
            return [0]
        g = {i: [] for i in range(n)}
        for e in edges:
            g[e[0]].append(e[1])
            g[e[1]].append(e[0])

        dis1 = {i: None for i in range(n)}

        def dfs1(i, v):
            if dis1[i] != None:
                return
            dis1[i] = v
            for c in g[i]:
                dfs1(c, v + 1)

        s = [k for k, v in g.items() if len(v) == 1][0]

        dfs1(s, 0)
        m1 = max([(v, k) for k, v in dis1.items()])[1]
        for i in range(n):
            dis1[i] = None
        dfs1(m1, 0)
        m2 = max([(v, k) for k, v in dis1.items()])[1]

        stack = [m1]
        path = {0: None}

        def dfs2(i, p):
            for c in g[i]:
                if c != p:
                    stack.append(c)
                    if stack[-1] == m2:
                        path[0] = list(stack)
                    dfs2(c, i)
                    stack.pop()

        dfs2(m1, None)
        path = path[0]

        if len(path) % 2 == 1:
            return [path[len(path) // 2]]
        else:
            return sorted([path[len(path) // 2 - 1], path[len(path) // 2]])
