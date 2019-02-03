# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e


class Solution:
    def intervalIntersection(
        self, A: "List[Interval]", B: "List[Interval]"
    ) -> "List[Interval]":
        i = 0
        j = 0
        out = []

        def intersects(a, b):
            if a.end < b.start:
                return True, False, None
            elif b.end < a.start:
                return False, True, None
            else:
                return (
                    a.end <= b.end,
                    b.end <= a.end,
                    Interval(max(a.start, b.start), min(a.end, b.end)),
                )

        while i < len(A) and j < len(B):
            inci, incj, newitv = intersects(A[i], B[j])
            if newitv is not None:
                out.append(newitv)
            if inci:
                i += 1
            if incj:
                j += 1
        return out
