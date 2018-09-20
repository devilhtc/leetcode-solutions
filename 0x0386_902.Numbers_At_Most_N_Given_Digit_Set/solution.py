class Solution(object):
    def atMostNGivenDigitSet(self, D, N):
        """
        :type D: List[str]
        :type N: int
        :rtype: int
        """
        self.D = D
        Ns = str(N)
        mag = len(Ns) - 1
        base = 0

        # all the numbers that is shorter
        for i in range(mag):
            base += self.certainLen(i + 1)

        return base + self.sameLen(Ns)

    def certainLen(self, l):
        return len(self.D) ** l

    def sameLen(self, Ns):
        """
        return the number of numbers that has the
        same length as Ns (a string repr of int)
        """
        if len(Ns) == 0:
            return 1
        if Ns.startswith("0"):
            return 0
        lead = Ns[0]  # must not be 0
        mag = len(Ns) - 1
        x = len([1 for ele in self.D if int(ele) < int(lead)])
        base = x * self.certainLen(mag)
        extra = 0 if lead not in self.D else self.sameLen(Ns[1:])
        return base + extra
