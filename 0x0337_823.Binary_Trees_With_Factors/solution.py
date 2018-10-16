MOD = 1000000007


class Solution:
    def numFactoredBinaryTrees(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        A = sorted(A)
        v2i = {v: i for i, v in enumerate(A)}
        dp = []
        out = 0
        for i, v in enumerate(A):
            cur = 1
            for j in range(i):
                if A[j] ** 2 > v:
                    break
                a, b = A[j], v // A[j]
                if v % A[j] == 0 and b in v2i:
                    k = v2i[b]
                    if a == b:
                        cur = (cur + dp[j] ** 2) % MOD
                    else:
                        cur = (cur + dp[j] * dp[k] * 2) % MOD
            dp.append(cur)
            out = (out + cur) % MOD
        return out
