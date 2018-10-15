class Solution:
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """
        m = c = 0
        for s in S:
            c += 1 if s == "(" else -1
            m = min(m, c)
        return c - 2 * m
