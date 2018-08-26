class Solution:
    def numSpecialEquivGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        t = set([])
        for s in A:
            sig = self.getSig(s)
            t.add(sig)
        return len(t)

    def getSig(self, s):
        return "".join(
            sorted([s[i] for i in range(len(s)) if i % 2 == 0])
            + sorted([s[i] for i in range(len(s)) if i % 2 == 1])
        )
