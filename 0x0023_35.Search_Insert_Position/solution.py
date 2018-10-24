class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if target <= nums[0]:
            return 0
        if target >= nums[-1]:
            return len(nums) - (1 if target == nums[-1] else 0)

        lo = 0
        hi = len(nums)
        while hi > lo + 1:
            mi = (hi + lo) // 2
            if nums[mi] == target:
                return mi
            elif nums[mi] > target:
                hi = mi
            else:
                lo = mi
        return hi
