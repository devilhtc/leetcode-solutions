class Solution(object):
    def largestOverlap(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: int
        """
        Aones = []
        Bones = []
        m, n = len(A), len(A[0])
        for i in range(m):
            for j in range(n):
                if A[i][j]:
                    Aones.append((i, j))
                if B[i][j]:
                    Bones.append((i, j))
        if len(Aones) == 0 or len(Bones) == 0:
            return 0
        d = collections.defaultdict(int)
        for i1, j1 in Aones:
            for i2, j2 in Bones:
                d[(i1 - i2, j1 - j2)] += 1

        return max(v for k, v in d.items())
