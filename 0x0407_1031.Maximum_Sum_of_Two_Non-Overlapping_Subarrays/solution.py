class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        cumsums, lmaxs, mmaxs = [0], [-1], [-1]
        out = -1
        for i, v in enumerate(A):
            cumsums.append(cumsums[-1] + v)
            if i >= L - 1:
                lmaxs.append(max(lmaxs[-1], cumsums[-1] - cumsums[-L - 1]))
            if i >= M - 1:
                mmaxs.append(max(mmaxs[-1], cumsums[-1] - cumsums[-M - 1]))
            if i >= M + L - 1:
                out = max(
                    out,
                    cumsums[-1] - cumsums[-M - 1] + lmaxs[-M - 1],
                    cumsums[-1] - cumsums[-L - 1] + mmaxs[-L - 1],
                )
        return out
