class Solution:
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp = [[False] * len(s) for _ in range(len(s))]
        out = 0
        l = len(s)
        for d in range(l):
            for i in range(l - d):
                if d == 0:
                    dp[i][i + d] = True
                elif d == 1:
                    dp[i][i + d] = s[i] == s[i + d]
                else:
                    dp[i][i + d] = s[i] == s[i + d] and dp[i + 1][i + d - 1]
                if dp[i][i + d]:
                    out += 1
        return out
