class Solution:
    def fixedPoint(self, A: List[int]) -> int:
        lo = 0
        hi = len(A) - 1
        while hi > lo + 1:
            mi = (hi + lo) // 2
            if A[mi] > mi:
                hi = mi - 1
            elif A[mi] == mi:
                hi = mi
            else:
                lo = mi
        if A[lo] == lo:
            return lo
        if A[hi] == hi:
            return hi
        return -1
