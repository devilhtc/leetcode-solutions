class UnionFind(object):
    def __init__(self, r, c):
        self.r = r
        self.c = c
        self.total = r * c + 1
        self.sizes = {i: 1 for i in range(self.total)}
        self.l = [i for i in range(self.total)]

    def union(self, a, b):
        a_id = self.coor2id(a)
        b_id = self.coor2id(b)
        a_an = self.findById(a_id)
        b_an = self.findById(b_id)
        if a_an == b_an:
            return
        lo, hi = (a_an, b_an) if a_an < b_an else (b_an, a_an)
        self.l[hi] = lo
        self.sizes[lo] = self.sizes[lo] + self.sizes.pop(hi)

    def find(self, a):
        i = self.coor2id(a)
        an = self.findById(i)
        self.l[i] = an
        return an

    def get_size(self, a):
        return self.sizes.get(self.coor2id(a), 0)

    def coor2id(self, coor):
        i, j = coor
        return 1 + i * self.c + j

    def findById(self, i):
        while self.l[i] != i:
            i = self.l[i]
        return i


class Solution(object):
    def hitBricks(self, grid, hits):
        """
        :type grid: List[List[int]]
        :type hits: List[List[int]]
        :rtype: List[int]
        """
        r, c = len(grid), len(grid[0])
        uf = UnionFind(r, c)
        hits_set = set(map(tuple, hits))
        brick_set = set(
            [
                (i, j)
                for i in range(r)
                for j in range(c)
                if grid[i][j] == 1 and (i, j) not in hits_set
            ]
        )

        for i in range(r):
            for j in range(c):
                if (i, j) in brick_set:
                    if i == 0:
                        uf.union((i, j), (0, -1))
                    if (i - 1, j) in brick_set:
                        uf.union((i, j), (i - 1, j))
                    if (i, j - 1) in brick_set:
                        uf.union((i, j), (i, j - 1))

        out = [0 for _ in range(len(hits))]

        for t in range(len(hits)):
            t2 = len(hits) - 1 - t
            i, j = tuple(hits[t2])
            if (i, j) in hits_set and grid[i][j] == 1:
                prevSize = uf.get_size((0, -1))
                if i == 0:
                    uf.union((i, j), (0, -1))
                for ii, jj in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                    if (ii, jj) in brick_set:
                        uf.union((i, j), (ii, jj))
                curSize = uf.get_size((0, -1))
                out[t2] = max(curSize - prevSize - 1, 0)
                brick_set.add((i, j))

        return out
