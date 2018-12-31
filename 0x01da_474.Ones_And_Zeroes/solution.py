class Solution:
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        d = collections.defaultdict(int)
        d[(0, 0)] = 0
        out = 0
        sc = collections.Counter(strs)
        for s, cc in sc.items():
            z, o = 0, 0
            for c in s:
                if c == "0":
                    z += 1
                else:
                    o += 1
            for k, v in list(d.items()):
                i, j = k
                for a in range(1, cc + 1):
                    if i + a * z <= m and j + a * o <= n:
                        d[(i + a * z, j + a * o)] = max(
                            d[(i + a * z, j + a * o)], v + a
                        )
                        out = max(d[(i + a * z, j + a * o)], out)
        return out
