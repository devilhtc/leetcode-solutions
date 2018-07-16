# numpy soolution with bit vector by @StefanPochmann

import numpy as np


class Solution:
    def splitArraySameAverage(self, A):
        N, S = len(A), sum(A)
        p = np.zeros((N, S + 1), dtype=bool)
        p[0][0] = 1
        for a in A:
            p[1:, a:] |= np.array(p[:-1, : -a or None])
        return any(S * n % N == 0 and p[n][S * n / N] for n in range(1, N))
