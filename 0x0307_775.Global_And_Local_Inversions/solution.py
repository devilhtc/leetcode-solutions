class Solution(object):
    def isIdealPermutation(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if len(A) <= 2:
            return True
        m = A[0]
        for i in range(2, len(A)):
            if A[i] < m:
                return False
            m = max(m, A[i - 1])
        return True
