class Solution(object):
    def minSwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        l = len(A)
        noswap = [0]
        swap = [1]
        for i in range(1, len(A)):
            nn = noswap[-1] if (A[i] > A[i - 1] and B[i] > B[i - 1]) else l
            sn = swap[-1] if (A[i] > B[i - 1] and B[i] > A[i - 1]) else l
            noswap.append(min(nn, sn))
            ss = swap[-1] if (A[i] > A[i - 1] and B[i] > B[i - 1]) else l
            ns = noswap[-2] if (A[i] > B[i - 1] and B[i] > A[i - 1]) else l
            swap.append(min(ss, ns) + 1)
        return min(noswap[-1], swap[-1])
