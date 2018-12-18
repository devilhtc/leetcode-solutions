class Solution:
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        oob = 10001
        if reader.get(0) > oob:
            return -1
        hi = 1
        while reader.get(hi) < oob:
            hi = hi * 2

        lo = 0

        while lo < hi:
            mi = (lo + hi) // 2
            if reader.get(mi) == target:
                return mi
            elif reader.get(mi) > target:
                hi = mi
            else:
                lo = mi + 1
        return -1
