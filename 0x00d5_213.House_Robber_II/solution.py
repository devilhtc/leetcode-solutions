class Solution:
    def rob(self, nums: "List[int]") -> "int":
        if len(nums) == 0:
            return 0
        if len(nums) <= 3:
            return max(nums)
        return max(
            self.rob_helper(nums, 0, len(nums) - 2),
            self.rob_helper(nums, 1, len(nums) - 1),
        )

    def rob_helper(self, nums, i, j):
        a, b = 0, nums[i]
        for k in range(i + 1, j + 1):
            a, b = max(a, b), a + nums[k]
        return max(a, b)
