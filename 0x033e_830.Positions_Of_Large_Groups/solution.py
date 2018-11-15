class Solution(object):
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        k = ""
        s = 0
        e = 0
        out = []
        for i, v in enumerate(S):
            if v == k:
                e = i
            else:
                if e - s >= 2:
                    out.append([s, e])
                k = v
                s = i
                e = i
            if i == len(S) - 1:
                if e - s >= 2:
                    out.append([s, e])
        return out
