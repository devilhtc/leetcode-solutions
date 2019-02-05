class Solution:
    def findNumberOfLIS(self, nums: "List[int]") -> "int":
        l = len(nums)
        if l == 0:
            return 0
        lengths = [1] * l
        counts = [1] * l
        for i in range(1, l):
            for j in range(i):
                if nums[i] > nums[j]:
                    cml = lengths[j] + 1
                    count = counts[j]
                    if cml > lengths[i]:
                        lengths[i] = cml
                        counts[i] = count
                    elif cml == lengths[i]:
                        counts[i] += count
        ml = max(lengths)
        return sum(counts[i] for i in range(l) if lengths[i] == ml)
