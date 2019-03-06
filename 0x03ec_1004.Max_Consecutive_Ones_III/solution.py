class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        j = 0
        m = 0
        out = 0
        for i, v in enumerate(A):
            while j < len(A):
                if A[j] == 1:
                    j += 1
                else:
                    if m < K:
                        m += 1
                        j += 1
                    else:
                        break
            out = max(out, j - i)
            if v == 0:
                m -= 1
        return out
