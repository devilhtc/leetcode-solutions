class Solution:
    def flipgame(self, fronts, backs):
        """
        :type fronts: List[int]
        :type backs: List[int]
        :rtype: int
        """
        l = len(fronts)
        bad = set()
        for i in range(l):
            if fronts[i] == backs[i]:
                bad.add(fronts[i])
        out = 0
        for i in range(2*l):
            num = fronts[i//2] if i % 2 == 0 else backs[i//2]
            if num not in bad:
                if out == 0:
                    out = num
                else:
                    out = min(num, out)
        return out
        