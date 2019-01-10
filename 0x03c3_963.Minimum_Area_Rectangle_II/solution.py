class Solution:
    def minAreaFreeRect(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        c = collections.defaultdict(list)
        p = points
        n = len(points)
        for i in range(n):
            for j in range(i + 1, n):
                cx = p[i][0] + p[j][0]
                cy = p[i][1] + p[j][1]
                cxy = (p[i][0] - p[j][0]) ** 2 + (p[i][1] - p[j][1]) ** 2
                if p[j][0] == p[i][0]:
                    t = float('inf')
                else:
                    t = (p[j][1] - p[i][1]) / (p[j][0] - p[i][0])
                
                c[(cx, cy, cxy)].append(t)
                
        def t2sc(t):
            if t == float('inf'):
                return 1.0, 0.0
            else:
                return t / math.sqrt(t ** 2 + 1), 1 / math.sqrt(t ** 2 + 1)
        
        out = float('inf')
        for k, v in c.items():
            if len(v) <= 1:
                continue
            _, _, cxy = k
            v = sorted(v)
            
            for i in range(len(v)):
                t1, t2 = v[i], v[(i + 1) % len(v)]
                s1, c1 = t2sc(t1)
                s2, c2 = t2sc(t2)
                s = abs(s1 * c2 - s2 * c1)
                out = min(out, s * cxy / 2)
                
        return 0.0 if out == float('inf') else float(round(out))
            
                