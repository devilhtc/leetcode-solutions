VOWELS = set(list("aeiouAEIOU"))


class Solution:
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        return " ".join([self.helper(v, i) for i, v in enumerate(S.split())])

    def helper(self, w, i):
        if w[0] not in VOWELS:
            w = w[1:] + w[0]
        return w + "maa" + "a" * i
