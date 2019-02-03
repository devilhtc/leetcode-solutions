class Solution:
    def findPermutation(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        base = 1
        ds = 0
        us = 0
        i = 0
        out = []
        p = True
        while i < len(s) + 1:
            c = s[i] if i < len(s) else "."
            if (c == "I" and ds > 0) or c == ".":
                for j in range(us - (0 if p else 1)):
                    out.append(base + j)
                for k in range(ds + 1):
                    out.append(us + ds + base - k - (0 if p else 1))
                base = base + us + ds + 1 - (0 if p else 1)
                p = False
                ds = 0
                us = 1
            elif s[i] == "I":
                us += 1
            else:
                ds += 1
            i += 1
        return out
