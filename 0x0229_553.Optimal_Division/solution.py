class Solution(object):
    def optimalDivision(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        joinDivision = lambda l: '/'.join(list(map(str,l)))
        if len(nums) == 1:
            return str(nums[0])
        if len(nums) == 2:
            return joinDivision(nums)
        return str(nums[0]) if len(nums) == 1 else str(nums[0]) + '/(' + joinDivision(nums[1:]) +')'