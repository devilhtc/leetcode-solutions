class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        a, b = numerator, denominator

        def signpart(a, b):
            return "-" if a * b < 0 else "", abs(a), abs(b)

        def intpart(a, b):
            c = a // b
            return str(c), a - b * c

        def floatpart(a, b):
            if a == 0:
                return ""
            nums = []
            dp = {}
            i = 0
            while a > 0:
                if a in dp:
                    out = []
                    for i in range(len(nums)):
                        if i == dp[a]:
                            out.append("(")
                        out.append(nums[i])
                    out.append(")")
                    return "." + "".join(out)
                c, d = divmod(a * 10, b)
                dp[a] = i
                i += 1

                if c == 0:
                    nums.append("0")
                    a = a * 10
                else:
                    nums.append(str(c))
                    a = d
            return "." + "".join(nums)

        sp, a, b = signpart(a, b)
        ip, a = intpart(a, b)
        fp = floatpart(a, b)

        return sp + ip + fp
