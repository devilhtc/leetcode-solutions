class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        l = len(A)
        if l == 0:
            return -1

        def countMinSwap(x):
            a = b = 0
            for i in range(l):
                if A[i] != x and B[i] != x:
                    return -1
                if A[i] != x:
                    a += 1
                if B[i] != x:
                    b += 1
            return min(a, b)

        y1 = countMinSwap(A[0])
        y2 = countMinSwap(B[0])
        if y1 == -1 and y2 == -1:
            return -1
        return min(y1 if y1 >= 0 else l + 1, y2 if y2 >= 0 else l + 1)
