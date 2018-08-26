class Solution:
    def advantageCount(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        A2, B2 = sorted(A), sorted([(v, i) for i, v in enumerate(B)])
        i, j = 0, len(A) - 1
        out = [0] * len(A)

        for ele in A2:
            if ele > B2[i][0]:
                out[B2[i][1]] = ele
                i += 1
            else:
                out[B2[j][1]] = ele
                j -= 1

        return out
