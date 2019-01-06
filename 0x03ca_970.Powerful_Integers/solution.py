class Solution:
    def powerfulIntegers(self, x, y, bound):
        """
        :type x: int
        :type y: int
        :type bound: int
        :rtype: List[int]
        """
        out = set([])
        i = 0
        j = 0
        while x ** i <= bound:
            j = 0
            while x ** i + y ** j <= bound:
                out.add(x ** i + y ** j)
                j += 1
                if y == 1:
                    break
            i += 1
            if x == 1:
                break
        return list(out)
