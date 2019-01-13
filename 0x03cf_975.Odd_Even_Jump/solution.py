class Solution:
    def oddEvenJumps(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        self.g_odd = {}
        self.g_even = {}
        self.odd_memo = {}
        self.even_memo = {}
        self.t = len(A) - 1

        Ab = sorted([(v, -i) for i, v in enumerate(A)])
        Af = sorted([(v, i) for i, v in enumerate(A)])

        for k in range(len(A)):
            _, bi = Ab[k]
            b = k - 1
            while b >= 0:
                v, i = Ab[b]
                if -i > -bi:
                    self.g_even[-bi] = -i
                    break
                b -= 1

            _, fi = Af[k]
            f = k + 1
            while f < len(A):
                v, i = Af[f]
                if i > fi:
                    self.g_odd[fi] = i
                    break
                f += 1

        return sum(self.dp(i, True) for i in range(len(A) - 1)) + 1

    def dp(self, i, odd):
        if odd:
            if i in self.odd_memo:
                return self.odd_memo[i]
            curg = self.g_odd
            curmemo = self.odd_memo
        else:
            if i in self.even_memo:
                return self.even_memo[i]
            curg = self.g_even
            curmemo = self.even_memo

        out = False

        if i in curg:
            if curg[i] == self.t:
                out = True
            else:
                out = self.dp(curg[i], not odd)

        curmemo[i] = out
        return out
