class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        ls, lp = len(s), len(p)
        dp = [[False] * (lp + 1) for _ in range(ls + 1)]
        dp[0][0] = True
        for j in range(lp):
            if p[j] == "*":
                dp[0][j + 1] = dp[0][j - 1]
        for i in range(ls):
            for j in range(lp):
                if p[j] == "*":
                    dp[i + 1][j + 1] = dp[i + 1][j - 1] or (
                        dp[i][j + 1] and (p[j - 1] == "." or p[j - 1] == s[i])
                    )
                elif p[j] == ".":
                    dp[i + 1][j + 1] = dp[i][j]
                else:
                    dp[i + 1][j + 1] = dp[i][j] and s[i] == p[j]
        return dp[-1][-1]
