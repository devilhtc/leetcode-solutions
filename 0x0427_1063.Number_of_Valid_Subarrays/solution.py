class Solution:
    def validSubarrays(self, nums: List[int]) -> int:
        stack = []
        min_val = min(nums)
        out = 0
        for v in nums + [min_val - 1]:
            while len(stack) > 0 and stack[-1] > v:
                x = stack.pop()
                out += len(stack)
            stack.append(v)
        return out + len(nums)
