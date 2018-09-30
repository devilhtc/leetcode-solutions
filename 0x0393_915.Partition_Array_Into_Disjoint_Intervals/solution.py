class Solution:
    def partitionDisjoint(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        l = len(A)
        lmax = [A[0]] * l
        rmin = [A[-1]] * l
        for i in range(1, l):
            j = l - 1 - i
            lmax[i] = max(lmax[i - 1], A[i])
            rmin[j] = min(rmin[j + 1], A[j])
        for i in range(l - 1):
            if lmax[i] <= rmin[i + 1]:
                return i + 1
        return l
