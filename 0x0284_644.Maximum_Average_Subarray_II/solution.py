class Solution:
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        if k == 1:
            return float(max(nums))
        self.nums = nums
        self.k = k
        lo = float(min(nums))
        hi = float(max(nums))
        error = 0.000005
        while hi - lo > error:
            mi = (hi + lo) / 2
            if self.hasSubarraySumGTE(mi):
                lo = mi
            else:
                hi = mi
        return lo

    def hasSubarraySumGTE(self, value):
        nums = self.nums
        k = self.k
        cs = 0.0
        cs2 = 0.0
        mcs2 = 0.0
        for i in range(k - 1):
            cs += nums[i] - value
        for j in range(k - 1, len(nums)):
            cs += nums[j] - value
            if cs >= mcs2:
                return True
            cs2 += nums[j - k + 1] - value
            mcs2 = min(cs2, mcs2)
        return False
