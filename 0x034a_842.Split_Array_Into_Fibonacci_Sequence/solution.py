class Solution:
    def splitIntoFibonacci(self, S):
        """
        :type S: str
        :rtype: List[int]
        """

        self.S = S
        l = len(S)
        for i in range(1, l // 2 + 1):
            for j in range(i + 1, l):
                c = self.helper(i, j)
                if len(c) > 2 and all(ele <= 2 ** 31 - 1 for ele in c):
                    return c
        return []

    def helper(self, i, j):
        a = self.parse_num(self.S[:i])
        b = self.parse_num(self.S[i:j])
        if a is None or b is None:
            return []
        out = [a, b]
        while j < len(self.S):
            c = a + b
            cs = str(c)
            if self.S[j : j + len(cs)] == cs:
                out.append(c)
                j = j + len(cs)
                a, b = b, c
            else:
                return []
        return out if len(out) >= 3 else []

    def parse_num(self, n):
        if n == "0":
            return 0
        elif n.startswith("0"):
            return None
        else:
            return int(n)
