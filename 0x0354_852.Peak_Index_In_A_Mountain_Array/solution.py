class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        mi = 0  # maximum index
        for i in range(len(A)):
            if A[i] > A[mi]:
                mi = i
        return mi
