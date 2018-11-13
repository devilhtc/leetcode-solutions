class Solution:
    def uniqueLetterString(self, S):
        """
        :type S: str
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        d = collections.defaultdict(list)
        for i, v in enumerate(S):
            d[v].append(i)

        out = 0
        for c, indices in d.items():
            for i, idx in enumerate(indices):
                if i == 0:
                    l = idx + 1
                else:
                    l = idx - indices[i - 1]

                if i == len(indices) - 1:
                    r = len(S) - idx
                else:
                    r = indices[i + 1] - idx
                out = (out + l * r) % MOD

        return out
