class Solution:
    def prisonAfterNDays(self, cells, N):
        """
        :type cells: List[int]
        :type N: int
        :rtype: List[int]
        """
        if N == 0:
            return cells

        def g(n, i):
            if i == -1:
                return 0
            if i == 6:
                return 0
            return (n >> (i)) & 1

        def step(n):
            out = 0
            for i in range(6):
                if g(n, i - 1) == g(n, i + 1):
                    out = out + (1 << i)
            return out

        N -= 1
        sig = 0

        for i in range(6):
            if cells[i] ^ cells[i + 2] == 0:
                sig = sig | (1 << i)

        d = {sig: 0}
        i = 0
        while True:
            sig = step(sig)
            i += 1
            if sig in d:
                p = i - d[sig]
                sig = [k for k, v in d.items() if v == N % p][0]
                break
            elif i == N:
                break

            d[sig] = i

        return [0] + [g(sig, i) for i in range(6)] + [0]
