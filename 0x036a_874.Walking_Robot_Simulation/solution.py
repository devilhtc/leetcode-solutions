class Solution:
    def robotSim(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """
        self.build(obstacles)

        md = 0
        loc = (0, 0)
        d = (0, 1)
        for c in commands:
            if c < 0:
                d = self.turn(d, c)
            else:
                loc = self.step(loc, d, c)
                md = max(md, loc[0] ** 2 + loc[1] ** 2)
        return md

    def turn(self, d, c):
        return (-d[1], d[0]) if c == -2 else (d[1], -d[0])

    def build(self, obstacles):
        dv, dh = {}, {}
        for o in obstacles:
            if o[0] not in dv:
                dv[o[0]] = []
            dv[o[0]].append(o[1])
            if o[1] not in dh:
                dh[o[1]] = []
            dh[o[1]].append(o[0])
        for k in dv:
            dv[k] = sorted(dv[k])
        for k in dh:
            dh[k] = sorted(dh[k])
        self.dv = dv
        self.dh = dh

    def step(self, s, d, u):
        if d[0] == 0:
            # stepping in vertical direction, x wont change
            return (s[0], self.stepHelper(self.dv, s[0], s[1], s[1] + u * d[1]))
        else:
            return (self.stepHelper(self.dh, s[1], s[0], s[0] + u * d[0]), s[1])

    def stepHelper(self, d, v, s, e):
        obstacles = d.get(v, [])
        s_lo, s_hi = self.bs(obstacles, s)
        e_lo, e_hi = self.bs(obstacles, e)
        if (
            e_lo == e_hi
            or s_lo != e_lo
            and not (s_lo == s_hi and e_lo != s_lo and e_lo != e_hi)  # false hit
        ):
            # hits obstacle
            if e > s:
                return obstacles[s_hi if s_lo != s_hi else s_hi + 1] - 1
            else:
                return obstacles[s_lo if s_lo != s_hi else s_lo - 1] + 1
        return e

    def bs(self, a, v):
        l = len(a)
        if l == 0:
            return (-1, 0)
        if v < a[0]:
            return (-1, 0)
        if v > a[-1]:
            return (l - 1, l)
        if v == a[0]:
            return (0, 0)
        if v == a[-1]:
            return (l - 1, l - 1)
        lo = 0
        hi = l - 1
        while hi - lo > 1:
            mi = (lo + hi) // 2
            if a[mi] == v:
                return (mi, mi)
            elif a[mi] < v:
                lo = mi
            else:
                hi = mi
        return (lo, hi)
