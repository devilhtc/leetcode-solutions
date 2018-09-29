class Solution:
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """

        br = list("{0:b}".format(N))
        cur = None
        out = 0
        for i, v in enumerate(br):
            if v == "1":
                if cur is None:
                    cur = i
                else:
                    out = max(out, i - cur)
                    cur = i
        return out
