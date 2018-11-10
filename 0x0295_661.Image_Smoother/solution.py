class Solution:
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        m, n = len(M), len(M[0])
        vw = lambda i, j: (M[i][j], 1) if (0 <= i < m and 0 <= j < n) else (0, 0)

        out = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                out[i][j] = (
                    lambda zipped: sum(ele[0] for ele in zipped)
                    // sum(ele[1] for ele in zipped)
                )(
                    [
                        vw(ii, jj)
                        for ii in range(i - 1, i + 2)
                        for jj in range(j - 1, j + 2)
                    ]
                )
        return out
