import re


def generateMaskedNumbers(l):
    return ("+" if l > 6 else "") + "*" * (l - 6) + ("-" if l > 6 else "") + "***-***-"


class Solution(object):
    def maskPII(self, S):
        """
        :type S: str
        :rtype: str
        """
        if "@" in S:
            return self.maskEmail(S)
        else:
            return self.maskPhone(S)

    def maskEmail(self, e):
        name1, name23 = tuple(e.split("@"))
        return name1[0].lower() + "*****" + name1[-1].lower() + "@" + name23.lower()

    def maskPhone(self, p):
        allNumbers = "".join([n for n in p if re.search("[0-9]", n) is not None])
        return generateMaskedNumbers(len(allNumbers) - 4) + allNumbers[-4:]
