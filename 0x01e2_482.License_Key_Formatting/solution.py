class Solution:
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        out = []
        c = 0
        for i in range(len(S) - 1, -1, -1):
            if S[i] == '-':
                continue
            else:
                c += 1
                out.append(S[i].upper())
                if c == K and i != 0:
                    out.append('-')
                    c = 0
        return ''.join(reversed(out)).strip('-')
        