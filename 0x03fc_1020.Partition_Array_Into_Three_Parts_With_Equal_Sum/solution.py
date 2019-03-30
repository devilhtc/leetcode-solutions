class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        s = sum(A)
        # cannot be divided into 3 parts
        if s % 3 != 0:
            return False
        f, cs = False, 0
        # f: whether we found the 1/3 point
        # cs: cummulative sum
        for i, ele in enumerate(A):
            cs += ele
            if cs == s // 3:
                f = True
            elif cs == (s // 3) * 2 and f and i < len(A) - 1:
                return True
        return False
