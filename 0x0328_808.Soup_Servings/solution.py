def _r(a):
    _u, _d = a
    y = min(_u, _d)
    x = max(_u, _d)
    while y:
        x, y = y, x % y
    return (_u // x, _d // x)

def _add(a, b):
    au, ad = a
    bu, bd = b
    o = (au * bd + ad * bu, ad * bd)
    return _r(o)

def _mul(a, b):
    au, ad = a
    bu, bd = b
    return _r((au * bu, ad * bd))


class Solution:
    def soupServings(self, N):
        """
        :type N: int
        :rtype: float
        """
        if N >= 5600:
            return 1.0
        self.memo = {}
        u, d = self.dp(N, N)
        return u / d

    def dp(self, A, B):
        if A <= 0 and B <= 0:
            return (1, 2)
        if A <= 0:
            return (1, 1)
        if B <= 0:
            return (0, 1)
        if (A, B) in self.memo:
            return self.memo[(A, B)]
        
        out = (0, 1)
        for r in [
            self.dp(A - 100, B),
            self.dp(A - 75, B - 25),
            self.dp(A - 50, B - 50),
            self.dp(A - 25, B - 75)
        ]:
            out = _add(
                out,
                _mul(
                    r,
                    (1, 4)
                )
            )
        self.memo[(A, B)] = out
        return out

        