class Solution:
    def anagramMappings(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        dA = collections.defaultdict(list)
        dB = collections.defaultdict(list)
        for i in range(len(A)):
            dA[A[i]].append(i)
            dB[B[i]].append(i)

        out = [0] * len(A)
        for k in dA:
            ai = dA[k]
            bi = dB[k]
            for i in range(len(ai)):
                out[ai[i]] = bi[i]
        return out
