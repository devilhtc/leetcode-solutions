class Solution:
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        dif = sum(A) - sum(B)
        sb = set(B)
        out = [0, 0]
        for i in A:
            if i - dif // 2 in sb:
                out = [i, i - dif // 2]
        return out
