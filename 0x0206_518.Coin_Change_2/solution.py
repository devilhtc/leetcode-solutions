class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        dp = [1] + [0] * amount
        for c in coins:
            for i in range(amount - c + 1):
                dp[i + c] = dp[i + c] + dp[i]
        return dp[amount]
