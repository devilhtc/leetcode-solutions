class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        dps = [{}]
        l = len(A)
        if l == 0:
            return 0
        out = 1
        for i in range(1, l):
            cdp = {}
            for j in range(i):
                d = A[i] - A[j]
                cdp[d] = max(dps[j].get(d, 1) + 1, cdp.get(d, 2))
                out = max(cdp[d], out)
            dps.append(cdp)
        return out
