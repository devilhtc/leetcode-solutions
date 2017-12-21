class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 0: return s
        dp = [[False for _ in range(len(s))] for _ in range(len(s))]
        for i in range(len(s)): dp[i][i] = True
        start, end = 0, 0
        for diff in range(1, len(s)):
            for i in range(len(s) - diff):
                if s[i] == s[i + diff] and (dp[i + 1][i + diff - 1] or diff == 1):
                    dp[i][i+diff] = True
                    start, end = i, i + diff
        return s[start: end + 1]