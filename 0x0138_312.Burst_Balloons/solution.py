class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        memo = {}

        def dp(i, j):
            if i > j:
                return 0

            if (i, j) in memo:
                return memo[(i, j)]

            out = 0
            l = 1 if i == 0 else nums[i - 1]
            r = 1 if j == len(nums) - 1 else nums[j + 1]
            for k in range(i, j + 1):
                out = max(out, l * nums[k] * r + dp(i, k - 1) + dp(k + 1, j))
            memo[(i, j)] = out
            return out

        out = dp(0, len(nums) - 1)

        return out
