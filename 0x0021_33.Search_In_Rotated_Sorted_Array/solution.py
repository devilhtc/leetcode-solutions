class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return -1
        lo, hi = 0, len(nums) - 1
        if nums[0] == target:
            return 0
        elif nums[-1] == target:
            return len(nums) - 1
        # lo, hi will never be the index found
        while lo < hi - 1: 
            mi = (lo + hi) // 2
            # lo, hi, mi will never be the same
            if nums[mi] == target:
                return mi
            elif nums[lo] < nums[mi] < nums[hi]:
                if nums[lo] < target < nums[mi]:
                    hi = mi
                else:
                    lo = mi
            elif nums[mi] > nums[lo] > nums[hi]:
                if nums[lo] < target < nums[mi]:
                    hi = mi
                else:
                    lo = mi
            else: # now nums[lo] > nums[hi] > nums[mi]:
                if nums[mi] < target < nums[hi]:
                    lo = mi
                else:
                    hi = mi

        return -1