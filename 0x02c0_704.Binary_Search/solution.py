class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        if len(nums) == 0:
            return -1
        if nums[0] == target:
            return 0
        if nums[-1] == target:
            return len(nums) - 1

        lo = 0
        hi = len(nums) - 1
        while hi > lo:
            mi = (hi + lo) // 2
            if nums[mi] == target:
                return mi
            elif nums[mi] < target:
                lo = mi + 1
            else:
                hi = mi

        return -1
