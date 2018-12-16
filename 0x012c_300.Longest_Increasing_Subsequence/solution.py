import random


class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if random.randint(0, 1) == 0:
            return self.method1(nums)
        else:
            return self.method2(nums)

    def method1(self, nums):
        if len(nums) == 0:
            return 0
        l = len(nums)
        dp = [1] * len(nums)
        for i in range(1, l):
            curmax = 1
            for j in range(i):
                if nums[i] > nums[j]:
                    curmax = max(curmax, dp[j] + 1)
            dp[i] = curmax
        return max(dp)

    def method2(self, nums):
        if len(nums) == 0:
            return 0
        l = len(nums)
        dp = [0] * l
        dp[0] = nums[0]
        i = 0
        for k in range(1, l):
            n = nums[k]
            if n > dp[i]:
                dp[i + 1] = n
                i += 1
            elif n < dp[0]:
                dp[0] = n
            else:
                lo = 0
                hi = i
                while hi > lo:
                    mi = (hi + lo) // 2
                    if dp[mi] < n:
                        lo = mi + 1
                    else:
                        hi = mi
                dp[lo] = n

        return i + 1
