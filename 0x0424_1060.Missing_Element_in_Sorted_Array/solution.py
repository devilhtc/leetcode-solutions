class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        # helper function:
        # get the number of missing element up to the x-th element
        get_missing = lambda x: nums[x - 1] - nums[0] + 1 - x

        # if the missing element is larger than the last element
        x = get_missing(len(nums))
        if k > x:
            return nums[-1] + (k - x)

        # if the missing element must be within the range
        # of (nums[0], nums[-1])
        lo = 0
        hi = len(nums) - 1
        while hi - lo > 1:
            mi = (hi + lo) // 2
            x = get_missing(mi + 1)
            if k > x:
                lo = mi
            else:
                hi = mi
        x = get_missing(lo + 1)
        return nums[lo] + (k - x)
