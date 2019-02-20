class Solution:
    def arrangeCoins(self, n: "int") -> "int":
        def isgood(k):
            return k * (k + 1) <= 2 * n < (k + 1) * (k + 2)

        base = int(math.sqrt(n * 2))
        for i in range(base - 1, base + 2):
            if isgood(i):
                return i
        return base + 2
