class Solution:
    def subarraysDivByK(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        dp = [0] * K
        dp[0] = 1
        cumsum = 0
        out = 0
        for ele in A:
            cumsum += ele
            out += dp[cumsum % K]
            dp[cumsum % K] += 1
        return out
