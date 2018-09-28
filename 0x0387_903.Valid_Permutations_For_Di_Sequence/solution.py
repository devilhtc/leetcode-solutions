class Solution(object):
    MOD = 1000000007

    def numPermsDISequence(self, S):
        """
        :type S: str
        :rtype: int
        """
        self.memo = {}
        self.nCr_memo = {}
        out = self.dp(S)
        return out

    def dp(self, s):
        if s in self.memo:
            return self.memo[s]
        out = 1
        if len(s) > 1:
            out = 0
            for i in range(len(s) + 1):
                if self.canbemax(s, i):
                    m = self.nCr(len(s), i)
                    if i == 0:
                        out += self.dp(s[1:]) * m
                    elif i == len(s):
                        out += self.dp(s[:-1]) * m
                    else:
                        out += self.dp(s[: i - 1]) * self.dp(s[i + 1 :]) * m
                    out = out % self.MOD
        self.memo[s] = out
        return out

    def canbemax(self, s, i):
        if i == 0:
            return s[0] == "D"
        elif i == len(s):
            return s[-1] == "I"
        else:
            return s[i - 1] == "I" and s[i] == "D"

    def nCr(self, n, r):
        if r == 0 or r == n:
            return 1
        key = (n, min(r, n - r))
        if key in self.nCr_memo:
            return self.nCr_memo[key]
        out = self.nCr(n - 1, r - 1) + self.nCr(n - 1, r)
        self.nCr_memo[key] = out
        return out
