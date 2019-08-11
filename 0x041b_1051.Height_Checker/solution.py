class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        heights2 = sorted(heights)
        return sum(1 for i in range(len(heights)) if heights[i] != heights2[i])
