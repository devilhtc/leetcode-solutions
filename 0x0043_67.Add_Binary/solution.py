class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        out = []
        c = 0
        for i in range(1, 1 + max(len(a), len(b))):
            ai = int(a[-i]) if i <= len(a) else 0
            bi = int(b[-i]) if i <= len(b) else 0
            s = ai + bi + c
            out.append(str(s % 2))
            c = s // 2
        if c != 0:
            out.append("1")
        return "".join(reversed(out))
