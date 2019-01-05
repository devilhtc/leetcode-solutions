class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 1

        def decode1(c):
            if c == "0":
                return 0
            if c == "*":
                return 9
            return 1

        if len(s) == 1:
            return decode1(s)

        def decode2(c1, c2):
            if c1 == "*" and c2 == "*":
                return 15
            if c1 == "*":
                if 0 <= int(c2) <= 6:
                    return 2
                else:
                    return 1
            if c2 == "*":
                if c1 == "1":
                    return 9
                elif c1 == "2":
                    return 6
                else:
                    return 0
            if c1 == "0":
                return 0

            return 1 if 10 <= int(c1 + c2) <= 26 else 0

        a, b = 1, decode1(s[0])
        MOD = 1000000007
        s = list(s)
        for i in range(2, len(s) + 1):
            a, b = b, (a * decode2(s[i - 2], s[i - 1]) + b * decode1(s[i - 1])) % MOD

        return b
