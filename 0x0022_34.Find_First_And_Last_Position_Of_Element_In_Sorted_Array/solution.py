class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # trivial cases
        if len(nums) == 0:
            return [-1, -1]
        if nums[0] > target or nums[-1] < target:
            return [-1, -1]
        if len(nums) == 1:
            return [-1, -1] if target != nums[0] else [0, 0]

        first = -1
        lo = 0
        hi = len(nums) - 1
        while hi >= lo:
            mi = (hi + lo) // 2
            if nums[mi] == target:
                if mi == 0 or nums[mi - 1] != target:
                    first = mi
                    break
                else:
                    hi = mi - 1
            elif nums[mi] < target:
                lo = mi + 1
            else:
                hi = mi - 1

        if first == -1:
            return [-1, -1]

        lo = first
        hi = len(nums) - 1
        while hi >= lo:
            mi = (hi + lo) // 2
            if nums[mi] == target:
                if mi == len(nums) - 1 or nums[mi] != target:
                    return [first, mi]
                else:
                    lo = mi + 1
            else:
                hi = mi - 1
        return [first, hi]
