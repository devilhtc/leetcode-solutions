class Solution:
    def sumSubseqWidths(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        MOD = 1000000007
        memo = {0: 0}

        def choose(i):
            if i in memo:
                return memo[i]
            else:
                out = ((choose(i - 1) + 1) * 2 - 1) % MOD
                memo[i] = out
                return out

        l = len(A)
        d = collections.defaultdict(int)
        for e in A:
            d[e] += 1

        A2 = sorted([(v, c) for v, c in d.items()])
        pre = 0
        out = 0
        for v, c in A2:
            out = (out + (choose(pre) - choose(l - pre - c)) * v * choose(c)) % MOD
            pre += c
        return out
