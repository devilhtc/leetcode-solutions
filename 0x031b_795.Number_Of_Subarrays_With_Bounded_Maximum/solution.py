class Solution(object):
    def numSubarrayBoundedMax(self, A, L, R):
        """
        :type A: List[int]
        :type L: int
        :type R: int
        :rtype: int
        """
        self.A = A
        self.L = L
        self.R = R
        p = -1
        out = 0
        for i, v in enumerate(A):
            if v > R:
                if p == -1:
                    continue
                else:
                    out += self.getCombInRange(p, i - 1)
                    p = -1
            else:
                if p == -1:
                    p = i
                if i == len(A) - 1:
                    out += self.getCombInRange(p, i)
        return out

    def getCombInRange(self, i, j):
        out = (j - i + 2) * (j - i + 1) // 2
        p = -1
        for k in range(i, j + 1):
            if self.A[k] < self.L:
                if p == -1:
                    p = k
                if k == j:
                    out -= (k - p + 2) * (k - p + 1) // 2
            else:
                if p == -1:
                    continue
                else:
                    out -= (k - p + 1) * (k - p) // 2
                    p = -1
        return out
