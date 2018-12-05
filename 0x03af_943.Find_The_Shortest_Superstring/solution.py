class Solution:
    """
    Note: TLE but it's correct
    """

    def shortestSuperstring(self, A):
        """
        :type A: List[str]
        :rtype: str
        """
        if len(A) == 0:
            return ""
        g = {}
        l = len(A)
        for i, a in enumerate(A):
            for j in range(i + 1, l):
                b = A[j]
                a2b, b2a = self.helper(a, b)
                g[(i, j)] = a2b
                g[(j, i)] = b2a

        self.g = g
        self.l = l
        self.optcost = 0
        self.opt = list(range(l))
        self.curcost = 0
        self.cur = []
        self.unvisited = set(range(l))
        for i in range(l):
            self.dfs(i)
        outputs = [A[self.opt[0]]]
        for i in range(l - 1):
            outputs.append(A[self.opt[i + 1]][self.g[(self.opt[i], self.opt[i + 1])] :])
        return "".join(outputs)

    def dfs(self, i):
        self.unvisited.remove(i)
        self.cur.append(i)
        if len(self.unvisited) == 0:
            if self.curcost > self.optcost:
                self.opt = list(self.cur)
                self.optcost = self.curcost
        else:
            for j in list(self.unvisited):
                edge_cost = self.g[(i, j)]
                self.curcost += edge_cost
                self.dfs(j)
                self.curcost -= edge_cost
        self.cur.pop()
        self.unvisited.add(i)

    def helper(self, a, b):
        la, lb = len(a), len(b)
        dp = [[0] * (lb + 1) for _ in range(la + 1)]
        for i in range(la):
            for j in range(lb):
                if a[i] == b[j]:
                    dp[i + 1][j + 1] = dp[i][j] + 1

        return (
            max(dp[-1][j] for j in range(lb + 1) if dp[-1][j] == j),
            max(dp[i][-1] for i in range(la + 1) if dp[i][-1] == i),
        )
