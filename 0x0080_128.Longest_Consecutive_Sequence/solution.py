class Solution:
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        out = 0
        d = {}
        for n in nums:
            if n in d:
                continue
            d[n] = n
            if n - 1 in d:
                lo = d[n - 1]
            else:
                lo = n
            if n + 1 in d:
                hi = d[n + 1]
            else:
                hi = n

            d[lo] = hi
            d[hi] = lo
            out = max(out, hi - lo + 1)
        return out
