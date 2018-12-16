# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):


class Solution(object):
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        o = 0
        temp = [""] * 4
        while n > 0:
            c = read4(temp)
            k = min(n, c)
            for i in range(k):
                buf[o + i] = temp[i]
            o += k
            n -= 4
        return o
