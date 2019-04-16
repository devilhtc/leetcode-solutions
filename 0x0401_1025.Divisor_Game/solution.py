class Solution:
    def divisorGame(self, N: int) -> bool:
        memo = {1: False}

        def dp(i):
            if i in memo:
                return memo[i]
            k = 1
            w = False
            while k * k <= i:
                if i % k != 0:
                    k += 1
                    continue
                if not dp(i - k):
                    w = True
                if k > 1 and not dp(i - i // k):
                    w = True
                k += 1
            memo[i] = w
            return w

        return dp(N)
