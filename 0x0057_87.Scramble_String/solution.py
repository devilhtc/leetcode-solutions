class Solution:
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        self.memo = {}
        return self.helper(s1, s2)

    def helper(self, s1, s2):
        k = s1 + "," + s2
        if k in self.memo:
            return self.memo[k]
        out = False
        if s1 == s2:
            out = True
        elif self.gensig(s1) != self.gensig(s2):
            out = False
        else:
            for i in range(1, len(s1)):
                if out:
                    break
                l1, r1 = s1[:i], s1[i:]
                l2, r2 = s2[:i], s2[i:]
                if self.helper(l1, l2) and self.helper(r1, r2):
                    out = True
                if out:
                    break
                l1, r1 = s1[-i:], s1[:-i]
                if self.helper(l1, l2) and self.helper(r1, r2):
                    out = True
        self.memo[k] = out
        return out

    def gensig(self, s):
        return "".join(sorted(list(s)))
