class Solution:
    def minimumDeleteSum(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        l1 = len(s1)
        l2 = len(s2)
        dp = [[0] * (l2 + 1) for _ in range(l1 + 1)]
        for i in range(l1):
            for j in range(l2):
                if s1[i] == s2[j]:
                    dp[i + 1][j + 1] = dp[i][j] + ord(s1[i])
                dp[i + 1][j + 1] = max(
                    [
                        dp[i + 1][j + 1],
                        dp[i + 1][j],
                        dp[i][j + 1]
                    ]
                )
        
        return sum(ord(c1) for c1 in s1) + sum(ord(c2) for c2 in s2) - dp[-1][-1] * 2