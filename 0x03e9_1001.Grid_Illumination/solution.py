class Solution:
    def gridIllumination(
        self, N: int, lamps: List[List[int]], queries: List[List[int]]
    ) -> List[int]:
        rows = collections.defaultdict(int)
        cols = collections.defaultdict(int)
        a45s = collections.defaultdict(int)
        a135s = collections.defaultdict(int)
        ons = set()

        def turnon(i, j):
            if (i, j) in ons:
                return
            ons.add((i, j))
            rows[i] += 1
            cols[j] += 1
            a45s[i + j] += 1
            a135s[i - j] += 1

        def turnoff(i, j):
            if (i, j) not in ons:
                return
            ons.remove((i, j))
            rows[i] -= 1
            cols[j] -= 1
            a45s[i + j] -= 1
            a135s[i - j] -= 1

        def query(i, j):
            if rows[i] > 0 or cols[j] > 0 or a45s[i + j] > 0 or a135s[i - j] > 0:
                return 1
            return 0

        def inbounds(i, j):
            return 0 <= i < N and 0 <= j < N

        for i, j in lamps:
            turnon(i, j)

        out = []
        for i, j in queries:
            out.append(query(i, j))
            for di in range(-1, 2):
                for dj in range(-1, 2):
                    if inbounds(i + di, j + dj):
                        turnoff(i + di, j + dj)

        return out
