class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return -1
        
        total = sum(nums)
        preSum = 0
        curSum = total - nums[0]
        if curSum == preSum:
            return 0
        for i in range(1, len(nums)):
            preSum += nums[i-1]
            curSum -= nums[i]
            if preSum == curSum:
                return i
        return -1
            
        