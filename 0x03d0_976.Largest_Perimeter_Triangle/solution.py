class Solution:
    def largestPerimeter(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        A = sorted(A)
        out = 0
        for i in range(2, len(A)):
            if A[i - 2] + A[i - 1] > A[i]:
                out = A[i] + A[i - 1] + A[i - 2]
        return out
