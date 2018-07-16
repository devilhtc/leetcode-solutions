class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        if len(matrix) == 0:
            return True
        m, n = len(matrix), len(matrix[0])
        d = {}
        for i in range(m):
            d[i - 0] = matrix[i][0]
        for j in range(n):
            d[0 - j] = matrix[0][j]
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] != d[i - j]:
                    return False
        return True
