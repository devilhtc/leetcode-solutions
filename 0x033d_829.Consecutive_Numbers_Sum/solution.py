class Solution:
    def consecutiveNumbersSum(self, N):
        """
        :type N: int
        :rtype: int
        """
        out = 1
        x = 2
        while x * (x + 1) <= 2 * N:
            if x % 2 == 1:
                if N % x == 0:
                    out += 1
            else:
                if N % (x // 2) == 0 and (2 * N) // x % 2 == 1:
                    out += 1
            x += 1
        return out
