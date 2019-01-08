class Solution:
    def catMouseGame(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: int
        """
        n = len(graph)
        dp = collections.defaultdict(int)
        rem = {}
        q = collections.deque([])

        # m: mouse pos
        # c: cat pos
        # p: current player (1 if mouse, 2 if cat)

        MOUSE, CAT = 1, 2
        for m in range(n):
            for c in range(n):
                for p in [MOUSE, CAT]:
                    if m == 0:
                        q.append((m, c, p, MOUSE))
                        dp[(m, c, p)] = MOUSE
                    elif m == c and c > 0:
                        q.append((m, c, p, CAT))
                        dp[(m, c, p)] = CAT
                    if p == MOUSE:
                        rem[(m, c, p)] = len(graph[m])
                    else:
                        rem[(m, c, p)] = len(graph[c]) - (1 if 0 in graph[c] else 0)

        def parents(m, c, p):
            out = []
            if p == MOUSE:
                for c2 in graph[c]:
                    if c2 > 0:
                        out.append((m, c2, 3 - p))
            else:
                for m2 in graph[m]:
                    out.append((m2, c, 3 - p))
            return out

        # w: winner
        while len(q) > 0:
            m, c, p, w = q.popleft()
            for m2, c2, p2 in parents(m, c, p):
                if dp[(m2, c2, p2)] > 0:
                    continue
                if p2 == w:
                    dp[(m2, c2, p2)] = w
                    q.append((m2, c2, p2, w))
                else:
                    rem[(m2, c2, p2)] -= 1
                    if rem[(m2, c2, p2)] == 0:
                        dp[(m2, c2, p2)] = w
                        q.append((m2, c2, p2, w))

        return dp[(1, 2, 1)]
