class Solution:
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        sc = "a"
        tc = "a"
        i = len(S) - 1
        j = len(T) - 1
        while sc == tc and (i >= 0 or j >= 0):
            sc, i = self.nextchar(S, i)
            tc, j = self.nextchar(T, j)
            if sc != tc:
                return False
        return True

    def nextchar(self, s, i):
        t = 0
        while i >= 0:
            if s[i] == "#":
                t += 1
            elif t > 0:
                t -= 1
            else:
                return s[i], i - 1
            i -= 1
        return None, i
