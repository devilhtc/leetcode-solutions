class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        dp[0][0] = True
        for i in range(len(p)):
            if p[i] == "*":
                dp[0][i + 1] = True
            else:
                break
        for i, ci in enumerate(s):
            for j, cj in enumerate(p):
                if cj == "*":
                    dp[i + 1][j + 1] = dp[i][j] or dp[i][j + 1] or dp[i + 1][j]
                else:
                    dp[i + 1][j + 1] = dp[i][j] and (ci == cj or cj == "?")
        return dp[-1][-1]
