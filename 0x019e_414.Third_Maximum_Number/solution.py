class Solution:
    def thirdMax(self, nums: "List[int]") -> "int":
        maxes = [float("-inf")] * 3
        for n in nums:
            if n in maxes:
                continue
            if n > maxes[0]:
                maxes[0], maxes[1], maxes[2] = n, maxes[0], maxes[1]
            elif maxes[1] < n < maxes[0]:
                maxes[1], maxes[2] = n, maxes[1]
            elif n > maxes[2]:
                maxes[2] = n
        return maxes[0] if maxes[2] == float("-inf") else maxes[2]
