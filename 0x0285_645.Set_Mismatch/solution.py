class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        d = {i + 1: 0 for i in range(n)}
        for num in nums:
            d[num] += 1
        out = [0, 0]
        for i in range(1, n + 1):
            if d[i] == 2:
                out[0] = i
            elif d[i] == 0:
                out[1] = i
        return out