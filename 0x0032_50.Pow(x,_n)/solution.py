class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if x == 0.0:
            return 0.0 if n != 0 else 1.0
        self.memo = {1: x, 0: 1.0, -1: 1.0 / x}
        return self.helper(n)

    def helper(self, n):
        if n in self.memo:
            return self.memo[n]

        if n % 2 == 1:
            out = self.helper((n - 1) // 2) ** 2 * self.helper(1)
        else:
            out = self.helper(n // 2) ** 2
        self.memo[n] = out
        return out
