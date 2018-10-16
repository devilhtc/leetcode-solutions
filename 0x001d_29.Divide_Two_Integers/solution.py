class Solution:
    def mymult(self, d1, d2):
        out = 0
        b1 = bin(d1)[2:]
        b2 = bin(d2)[2:]
        for i, v in enumerate(list(reversed(b1))):
            out += int(b2 + "0" * i, 2) if v == "1" else 0
        return out

    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        # py3 ints are 64 bits so this is safe
        if dividend == -1 * (2 ** 31) and divisor == -1:
            return 2 ** 31 - 1
        if dividend == -1 * (2 ** 31) and divisor == 1:
            return -2 ** 31
        neg = False
        if dividend < 0:
            neg = not neg
            dividend = abs(dividend)
        if divisor < 0:
            neg = not neg
            divisor = abs(divisor)

        lo = 0
        hi = 2 ** 31
        while hi - lo > 1:
            mi = (hi + lo) // 2
            if self.mymult(divisor, mi) <= dividend:
                lo = mi
            else:
                hi = mi
        return (-1 if neg else 1) * lo
