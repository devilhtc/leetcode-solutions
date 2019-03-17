class Solution:
    def numDupDigitsAtMostN(self, N: int) -> int:
        # general idea:
        # count numbers <= N and have distinct digits

        def helper(leading, r):
            # count numbers with leading digits leading and r remaining digits
            if len(set(leading)) < len(leading):
                return 0
            return distinct2(r, len(leading))

        def distinct(n):
            # count numbers with n distinct digits
            return distinct2(n - 1, 1) * 9

        def distinct2(n, k):
            # count numbers with n distinct digits
            # with k digits already used
            if n == 0:
                return 1
            out = 1
            for i in range(n):
                out = out * (10 - k)
                k += 1
            return out

        # get all the digits from N
        x = N
        digits = []
        while x > 0:
            x, d = divmod(x, 10)
            digits.append(d)
        digits = list(reversed(digits))

        # count numbers with less digits
        le = 0
        for j in range(1, len(digits)):
            le += distinct(j)

        # count numbers with the same digits but < N
        leading = []
        for i, d in enumerate(digits):
            for x in range(1 if i == 0 else 0, d):
                leading.append(x)
                le += helper(leading, len(digits) - len(leading))
                leading.pop()
            leading.append(d)

        # have to -1 if N itself has distinct digits
        return N - le - (1 if len(set(digits)) == len(digits) else 0)
