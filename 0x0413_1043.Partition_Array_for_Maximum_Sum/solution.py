class Solution:
    def maxSumAfterPartitioning(self, A: List[int], K: int) -> int:
        l = len(A)
        memo = [0]
        for i in range(l):
            cm = -1
            v = -1
            for j in range(K):
                if i - j < 0:
                    continue
                cm = max(A[i - j], cm)
                v = max(memo[-j - 1] + cm * (j + 1), v)
            memo.append(v)
        return memo[-1]
