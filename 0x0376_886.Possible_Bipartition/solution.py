class Solution:
    def possibleBipartition(self, N, dislikes):
        """
        :type N: int
        :type dislikes: List[List[int]]
        :rtype: bool
        """
        # construct graph
        g = collections.defaultdict(list)
        for d in dislikes:
            a, b = d[0], d[1]
            g[a].append(b)
            g[b].append(a)

        # color 0: not processed, 1, 2: opposing, 3: contentious
        c = [0] * (N + 1)

        def dfs(i, v):
            if c[i] == 3:
                return
            if c[i] == 0:
                c[i] = v
                for d in g[i]:
                    dfs(d, 3 - v)
                return
            if c[i] != v:
                c[i] = 3

        for i in range(N + 1):
            if c[i] == 0:
                dfs(i, 1)

        return all(v != 3 for v in c)
