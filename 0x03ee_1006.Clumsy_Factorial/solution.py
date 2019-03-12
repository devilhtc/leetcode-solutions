class Solution:
    def clumsy(self, N: int) -> int:
        def helper(n, s):
            if n <= 4:
                if n <= 2:
                    return n * s, 0
                if n == 3:
                    return 6 * s, 0
                return 6 * s + 1, 0
            t1 = (n * (n - 1)) // (n - 2)
            return s * t1 + (n - 3), n - 4

        out = 0
        s = 1
        while N > 0:
            t, N = helper(N, s)
            s = -1
            out += t
        return out
