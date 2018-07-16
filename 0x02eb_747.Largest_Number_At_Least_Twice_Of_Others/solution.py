class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        largest = max(nums)
        k = -1
        for i in range(len(nums)):
            if nums[i] == largest:
                k = i
            else:
                if 2 * nums[i] > largest:
                    return -1
        return k
