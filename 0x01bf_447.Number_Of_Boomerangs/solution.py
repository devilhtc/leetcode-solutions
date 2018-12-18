class Solution:
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        out = 0
        for i, c in enumerate(points):
            d = collections.defaultdict(int)
            for j, p in enumerate(points):
                if j == i:
                    continue
                dis2 = (c[0] - p[0]) ** 2 + (c[1] - p[1]) ** 2
                d[dis2] += 1
            for k, v in d.items():
                out += v * (v - 1)
        return out
