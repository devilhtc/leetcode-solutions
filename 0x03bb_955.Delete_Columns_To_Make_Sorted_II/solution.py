class Solution(object):
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        m = len(A)
        n = len(A[0])
        s = set(range(m - 1))
        d = 0
        for i in range(n):
            nd = False
            ki = []
            for j in range(m - 1):
                if j not in s:
                    continue  # already sorted
                if A[j][i] > A[j + 1][i]:
                    nd = True
                elif A[j][i] < A[j + 1][i]:
                    ki.append(j)
            # print(i, nd, ki)
            if nd:
                d += 1
            else:
                for k in ki:
                    s.remove(k)
        return d
