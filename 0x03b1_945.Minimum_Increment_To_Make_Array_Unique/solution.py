class Solution:
    def minIncrementForUnique(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A) == 0:
            return 0
        A = sorted(A)
        e = A[0]
        out = 0
        for num in A:
            if num <= e:
                out += e - num
                e += 1
            else:
                e = num + 1
        return out
