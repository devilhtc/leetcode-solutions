class Solution:
    def strWithout3a3b(self, A, B):
        """
        :type A: int
        :type B: int
        :rtype: str
        """
        out = []
        pa, pb = 0, 0
        while A > 0 or B > 0:
            if A == 0:
                out.append("b")
                B -= 1
            elif B == 0:
                out.append("a")
                A -= 1
            elif A > B:
                if pa == 2:
                    out.append("b")
                    pa = 0
                    pb = 1
                    B -= 1
                else:
                    out.append("a")
                    pa += 1
                    A -= 1
            else:
                if pb == 2:
                    out.append("a")
                    pb = 0
                    pa = 1
                    A -= 1
                else:
                    out.append("b")
                    pb += 1
                    B -= 1
        return "".join(out)
