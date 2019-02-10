class Solution:
    def addToArrayForm(self, A: "List[int]", K: "int") -> "List[int]":
        i, c = len(A) - 1, 0
        n = K
        out = []

        while i >= 0 or n > 0 or c > 0:
            # get two numbers at this position
            a = A[i] if i >= 0 else 0
            b = n % 10

            # add
            s = a + b + c

            # put digit and calculate carry
            out.append(s % 10)
            c = s // 10

            # next step
            i -= 1
            n = n // 10

        return list(reversed(out))
