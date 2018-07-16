class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums = sorted(nums)
        if len(nums) < 3:
            return sum(nums)
        out = sum(nums[:3])
        minDis = abs(out - target)
        for i in range(len(nums) - 2):

            l = i + 1
            r = len(nums) - 1
            while l < r:
                curSum = nums[i] + nums[l] + nums[r]
                curDis = abs(target - curSum)
                if curSum == target:
                    return target
                if curDis < minDis:
                    minDis = curDis
                    out = curSum
                if curSum > target:
                    r -= 1
                else:
                    l += 1
        return out
