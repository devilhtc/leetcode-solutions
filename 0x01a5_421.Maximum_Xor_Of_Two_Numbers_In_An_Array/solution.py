class Solution:
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        gennode = lambda: {0: None, 1: None}
        bnums = ["{0:b}".format(x) for x in nums]
        maxlen = max(len(x) for x in bnums)
        bnums = ["0" * (maxlen - len(x)) + x for x in bnums]
        root = gennode()
        for n in bnums:
            cur = root
            for c in n:
                c = int(c)
                if not cur[c]:
                    cur[c] = gennode()
                cur = cur[c]

        out = 0
        for n in bnums:
            nmax = 0
            cur = root
            for c in n:
                c = int(c)
                if cur[1 - c]:
                    nmax = nmax * 2 + 1
                    cur = cur[1 - c]
                else:
                    nmax = nmax * 2
                    cur = cur[c]
            out = max(nmax, out)
        return out
