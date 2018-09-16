class Solution(object):
    def orderlyQueue(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        if K > 1:
            return "".join(sorted(list(S)))
        else:
            return self.minRot(S)

    def minRot(self, S):
        k = 0
        for i in range(len(S)):
            if self.compRot(i, k, S):
                k = i
        return S if k == 0 else S[k:] + S[:k]

    def compRot(self, i, j, S):
        # return t if rotation i <= j
        l = len(S)
        for k in range(l):
            a, b = S[(i + k) % l], S[(j + k) % l]
            if a != b:
                return a < b
        return True
