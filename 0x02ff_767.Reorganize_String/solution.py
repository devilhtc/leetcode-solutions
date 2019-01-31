class Solution:
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        mc = 0
        d = collections.defaultdict(int)
        for c in S:
            d[c] += 1
            mc = max(d[c], mc)
        if not mc <= (len(S) + 1) // 2:
            return ""

        out = [None] * len(S)
        i = 0
        for _, char, count in sorted([(-v, k, v) for k, v in d.items()]):
            for _ in range(count):
                out[i] = char
                i += 2
                if i >= len(S):
                    i = 1
        return "".join(out)
