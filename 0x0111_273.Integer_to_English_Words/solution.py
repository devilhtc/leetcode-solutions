class Solution:
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "Zero"

        digits = {
            1: "One",
            2: "Two",
            3: "Three",
            4: "Four",
            5: "Five",
            6: "Six",
            7: "Seven",
            8: "Eight",
            9: "Nine",
        }
        tys = {
            2: "Twenty",
            3: "Thirty",
            4: "Forty",
            5: "Fifty",
            6: "Sixty",
            7: "Seventy",
            8: "Eighty",
            9: "Ninety",
        }
        teens = {
            10: "Ten",
            11: "Eleven",
            12: "Twelve",
            13: "Thirteen",
            14: "Fourteen",
            15: "Fifteen",
            16: "Sixteen",
            17: "Seventeen",
            18: "Eighteen",
            19: "Nineteen",
        }
        rest, ones = divmod(num, 1000)
        rest, thousands = divmod(rest, 1000)
        rest, millions = divmod(rest, 1000)
        _, billions = divmod(rest, 1000)

        def pronounce(n):
            a, b = divmod(n, 100)
            out = []
            if a > 0:
                out.append(digits[a])
                out.append("Hundred")
            if b == 0:
                pass
            elif b < 10:
                out.append(digits[b])
            elif b in teens:
                out.append(teens[b])
            else:
                c, d = divmod(b, 10)
                out.append(tys[c])
                if d > 0:
                    out.append(digits[d])
            return " ".join(out)

        out = []

        if billions > 0:
            out.append(pronounce(billions))
            out.append("Billion")
        if millions > 0:
            out.append(pronounce(millions))
            out.append("Million")
        if thousands > 0:
            out.append(pronounce(thousands))
            out.append("Thousand")
        if ones > 0:
            out.append(pronounce(ones))

        return " ".join(out)
