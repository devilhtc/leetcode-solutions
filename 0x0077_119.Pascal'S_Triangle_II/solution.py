class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1]
        p = [0] * (rowIndex + 1)
        p[0] = 1
        n = [0] * (rowIndex + 1)
        for i in range(rowIndex):
            n[0] = 1
            n[i + 1] = 1
            for j in range(1, i + 1):
                n[j] = p[j - 1] + p[j]
            n, p = p, n
        return p
        