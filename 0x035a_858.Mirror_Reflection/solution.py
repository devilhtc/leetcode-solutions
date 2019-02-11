class Solution:
    def mirrorReflection(self, p, q):
        """
        :type p: int
        :type q: int
        :rtype: int
        """
        if q == p:
            return 1
        r = math.gcd(p, q)
        p //= r
        q //= r
        if p % 2 == 1 and q % 2 == 1:
            return 1
        if p % 2 == 0 and q % 2 == 1:
            return 2
        return 0
