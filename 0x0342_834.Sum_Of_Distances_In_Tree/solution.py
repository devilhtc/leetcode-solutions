class Solution(object):
    def sumOfDistancesInTree(self, N, edges):
        """
        :type N: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """

        # first step, generate a undirected graph
        self.g0 = [[] for _ in range(N)]
        for e in edges:
            a, b = tuple(e)
            self.g0[a].append(b)
            self.g0[b].append(a)

        # second step, generate a tree based on the graph
        # this won't change the result
        root = 0
        self.g = [[] for _ in range(N)]
        self.gen_tree(root, None)

        # third step, conduct pass1 to calculate the
        # number of child nodes and the sum of distances
        self.fc = [None for _ in range(N)]
        self.pass1(root)

        # fourth step, conduct pass2 to calculate the
        # number of parent nodes and the sum of distances
        self.fp = [None for _ in range(N)]
        self.fp[root] = (0, 0)
        self.pass2(root)

        return [self.fc[i][1] + self.fp[i][1] for i in range(N)]

    def gen_tree(self, i, p):
        for c in self.g0[i]:
            if c != p:
                self.g[i].append(c)
                self.gen_tree(c, i)

    def pass1(self, i):
        n = s = 0
        for c in self.g[i]:
            nc, sc = self.pass1(c)
            n += nc
            s += sc
        self.fc[i] = (n, s)
        return n + 1, s + n + 1

    def pass2(self, i):
        np, sp = self.fp[i]
        nc, sc = self.fc[i]
        for c in self.g[i]:
            n, s = self.fc[c]
            nx = np + nc - n - 1
            sx = sp + sc - n - s - 1
            self.fp[c] = (nx + 1, sx + nx + 1)
            self.pass2(c)
