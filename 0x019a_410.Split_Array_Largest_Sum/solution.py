class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        memo = {}
        l = len(nums)
        cumsum = [0]
        for ele in nums:
            cumsum.append(cumsum[-1] + ele)

        def findsum(i, j):
            return cumsum[j + 1] - cumsum[i]

        def dp(i, k):
            if i >= l:
                return float("inf")
            elif k == 1:
                return findsum(i, l - 1)
            elif k > l - i:
                return float("inf")

            if (i, k) in memo:
                return memo[(i, k)]

            out = float("inf")
            for j in range(i, l):
                out = min(out, max(dp(j + 1, k - 1), findsum(i, j)))
            memo[(i, k)] = out
            return out

        return dp(0, m)
