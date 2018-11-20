class Solution(object):
    def loudAndRich(self, richer, quiet):
        """
        :type richer: List[List[int]]
        :type quiet: List[int]
        :rtype: List[int]
        """
        g = collections.defaultdict(list)
        for r in richer:
            g[r[1]].append(r[0])

        out = [-1] * len(quiet)

        def dfs(i):
            if out[i] >= 0:
                return out[i]
            r = i
            for c in g[i]:
                cq = dfs(c)
                if quiet[cq] < quiet[r]:
                    r = cq
            out[i] = r
            return r

        for i in range(len(quiet)):
            dfs(i)
        return out
