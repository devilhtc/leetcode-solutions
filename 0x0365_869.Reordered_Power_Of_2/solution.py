import math

OVERFLOW_BOUNDARY = 5 * int(
    math.pow(10, 8)
)  # if a number is larger than this, twice it gonna be overflow


def countDigits(i):
    d = {}
    for ele in str(i):
        d[ele] = d.get(ele, 0) + 1
    return d


class Solution:
    def reorderedPowerOf2(self, N):
        """
        :type N: int
        :rtype: bool
        """
        l = len(str(N))
        smallest = int(
            math.pow(10, l - 1)
        )  # smallest number that has the same length as N
        num = int(
            math.pow(2, int(math.log2(smallest)))
        )  # largest power of 2 that has length <= length of smallest
        dN = countDigits(N)  # the digits in N
        while True:
            d = countDigits(num)
            if d == dN:
                return True
            if num > OVERFLOW_BOUNDARY or len(str(num)) > l:
                break
            num = num * 2

        return False
