class Solution:
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return (
            s.count(".") <= 1
            and re.compile(
                "^\s*[-+]?[0-9\.]{" + str(s.count(".") + 1) + ",}(e[-+]?[0-9]+)?\s*$"
            ).search(s)
            is not None
        )
