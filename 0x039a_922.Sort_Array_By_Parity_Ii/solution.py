class Solution:
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        i = 0
        j = 1
        n = len(A)
        while True:
            while i < n and A[i] % 2 == 0:
                i = i + 2
            while j < n and A[j] % 2 == 1:
                j = j + 2
            if i >= n or j >= n:
                break
            A[i], A[j] = A[j], A[i]
            i += 2
            j += 2
        return A
