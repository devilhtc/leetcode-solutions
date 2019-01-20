class Solution:
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        if len(A) <= 1 or (A[0] >= 0 and A[-1] >= 0):
            return [e ** 2 for e in A]
        if A[0] <= 0 and A[-1] <= 0:
            return [e ** 2 for e in reversed(A)]

        p = 0
        for i in range(len(A) - 1):
            if A[i] <= 0 and A[i + 1] >= 0:
                p = i
                break

        i = p
        j = p + 1
        out = []
        for t in range(len(A)):
            if i < 0:
                out.append(A[j] ** 2)
                j += 1
            elif j == len(A):
                out.append(A[i] ** 2)
                i -= 1
            else:
                if abs(A[i]) <= abs(A[j]):
                    out.append(A[i] ** 2)
                    i -= 1
                else:
                    out.append(A[j] ** 2)
                    j += 1
        return out
