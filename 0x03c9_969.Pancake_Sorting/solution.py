class Solution:
    def pancakeSort(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """

        def flip(k):
            i = 0
            j = k - 1
            while i <= j:
                A[i], A[j] = A[j], A[i]
                i += 1
                j -= 1

        out = []

        for i in range(len(A), 1, -1):
            k = A.index(i)
            if k != i - 1:
                flip(k + 1)
                flip(i)
                out.append(k + 1)
                out.append(i)
        #
        return out
