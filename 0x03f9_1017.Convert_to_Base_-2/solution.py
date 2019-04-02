class Solution:
    def baseNeg2(self, N: int) -> str:
        if N == 0:
            return "0"
        out = []
        while N != 0:
            if N % 2 == 1:
                N = (N - 1) // (-2)
                out.append("1")
            else:
                N = N // (-2)
                out.append("0")
        return "".join(reversed(out))
