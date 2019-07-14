class Solution:
    def numMovesStonesII(self, stones: List[int]) -> List[int]:
        n = len(stones)
        stones = sorted(stones)

        def compress(stones):
            last = stones[0]
            c = [1]  # compressed
            for i in range(1, n):
                s = stones[i]
                if s == last + 1:
                    c[-1] += 1
                else:
                    c.append(s - last - 1)
                    c.append(1)
                last = s
            return c

        def findmin(c):
            if len(c) == 1:
                return 0
            if len(c) == 3:
                if c[1] == 1:
                    return 1
                if c[0] == 1 or c[2] == 1:
                    return 2
                return sum(c) - n
            stones = 0
            spaces = 0
            i = 0
            out = n
            for j, s in enumerate(c):
                if j % 2 == 0:
                    stones += s
                else:
                    spaces += s
                if j % 2 == 1 and stones + spaces >= n:
                    candidates = [out, n - stones]
                    out = min(candidates)
                if j % 2 == 0 and stones + spaces >= n and stones + spaces - c[j] < n:
                    candidates = [out, spaces]
                    out = min(candidates)
                while j % 2 == 0 and stones + spaces >= n:
                    stones -= c[i]
                    spaces -= c[i + 1]
                    i += 2
            return out

        def findmax(c):
            if len(c) == 1:
                return 0
            spaces = sum(s for i, s in enumerate(c) if i % 2 == 1)
            if c[0] == 1 and c[-1] == 1:
                return spaces - min(c[1], c[-2])
            return spaces

        c = compress(stones)
        return [findmin(c), findmax(c)]
