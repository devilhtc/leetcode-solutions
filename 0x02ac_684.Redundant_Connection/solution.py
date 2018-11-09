class UF:
    def __init__(self):
        self.uf = {}

    def find(self, a):
        if a not in self.uf:
            self.uf[a] = a
            return a
        c = a
        while self.uf[c] != c:
            c = self.uf[c]

        self.uf[a] = c
        return c

    def union(self, a, b):
        fa = self.find(a)
        fb = self.find(b)
        root = min(fa, fb)
        self.uf[a] = root
        self.uf[b] = root


class Solution:
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        uf = UF()
        for e in edges:
            f1 = uf.find(e[0])
            f2 = uf.find(e[1])
            if f1 == f2:
                break
            else:
                uf.union(f1, f2)
        return e
