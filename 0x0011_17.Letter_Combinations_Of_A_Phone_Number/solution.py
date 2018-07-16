class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0:
            return []
        self.d = {}
        self.d["2"] = ["a", "b", "c"]
        self.d["3"] = ["d", "e", "f"]
        self.d["4"] = ["h", "g", "i"]
        self.d["5"] = ["j", "k", "l"]
        self.d["6"] = ["m", "n", "o"]
        self.d["7"] = ["p", "q", "r", "s"]
        self.d["8"] = ["t", "u", "v"]
        self.d["9"] = ["w", "x", "y", "z"]
        return self.helper(digits)

    def helper(self, digits):
        if len(digits) == 1:
            return self.d[digits]
        suffixes = self.helper(digits[1:])
        prefixes = self.d[digits[0]]
        return [pre + suf for pre in prefixes for suf in suffixes]
