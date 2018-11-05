class Solution:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        # trivial case
        if num1 == "0" or num2 == "0":
            return "0"

        # base case
        if len(num1) < 3 and len(num2) < 3:
            a = int(num1[0]) if len(num1) == 2 else 0
            b = int(num1[-1])
            c = int(num2[0]) if len(num2) == 2 else 0
            d = int(num2[-1])
            return str(100 * a * c + 10 * (b * c + a * d) + b * d)

        # recursive case
        l = max(len(num1), len(num2)) // 2
        a = num1[:-l] if len(num1) > l else "0"
        b = num1[-l:] if len(num1) > l else num1
        c = num2[:-l] if len(num2) > l else "0"
        d = num2[-l:] if len(num2) > l else num2
        ac = self.multiply(a, c)  # a * c
        bd = self.multiply(b, d)  # b * d
        ad_bc = self.minus(  # a * d + b * c
            self.multiply(self.add(a, b), self.add(c, d)), self.add(ac, bd)
        )
        return self.add(
            self.add(self.shift(ac, 2 * l), bd), self.shift(ad_bc, l)
        ).lstrip("0")

    def add(self, num1, num2):
        if num1 == "0":
            return num2
        if num2 == "0":
            return num1
        out = []
        i = 1
        c = 0  # carry
        while i <= len(num1) or i <= len(num2):
            a = int(num1[-i]) if i <= len(num1) else 0
            b = int(num2[-i]) if i <= len(num2) else 0
            out.append(str((a + b + c) % 10))
            c = (a + b + c) // 10
            i += 1
        if c == 1:
            out.append("1")
        return "".join(reversed(out))

    def shift(self, num, digits):
        return num + "0" * digits

    def minus(self, num1, num2):
        if num2 == "0":
            return num1
        out = []
        i = 1
        c = 0  # carry
        while i <= len(num1) or i <= len(num2):
            a = int(num1[-i]) if i <= len(num1) else 0
            b = int(num2[-i]) if i <= len(num2) else 0
            out.append(str((a - b + c) % 10))
            c = -1 if (a - b + c) < 0 else 0
            i += 1
        return "".join(reversed(out))
