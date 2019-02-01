class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix)
        if m == 0:
            return False

        n = len(matrix[0])
        if n == 0:
            return False

        i = m - 1
        for j in range(n):
            while i >= 0:
                if matrix[i][j] > target:
                    i -= 1
                elif matrix[i][j] == target:
                    return True
                else:
                    break
        return False
