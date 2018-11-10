class Solution:
    def findRedundantDirectedConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        p = collections.defaultdict(list)
        nodes = set()
        can = []
        for i, e in enumerate(edges):
            u, v = tuple(e)
            if len(p[v]) > 0:  # double parent
                can.append(p[v][0][1])
                can.append(i)
            p[v].append((u, i))
            nodes.add(u)
            nodes.add(v)

        if len(can) == 2:
            if self.inloop(edges[can[0]], p):
                return edges[can[0]]
            elif self.inloop(edges[can[1]], p):
                return edges[can[1]]
            else:
                return edges[max(can)]

        # detect loop
        visited = collections.defaultdict(lambda: False)
        n = nodes.pop()
        while not visited[n]:
            visited[n] = True
            n = p[n][0][0]
        o = n

        idx = p[n][0][1]
        while p[n][0][0] != o:
            idx = max(p[n][0][1], idx)
            n = p[n][0][0]
        idx = max(p[n][0][1], idx)
        return edges[idx]

    def inloop(self, e, p):
        u, v = tuple(e)
        c = u
        while c in p:
            c = p[c][0][0]
            if c == v:
                return True
        return False
