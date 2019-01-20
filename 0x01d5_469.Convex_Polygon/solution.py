class Solution:
    def isConvex(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        if len(points) <= 3:
            return True
        angles = []
        for i, p in enumerate(points):
            np = points[0] if i == len(points) - 1 else points[i + 1]
            angles.append(math.atan2(np[1] - p[1], np[0] - p[0]))
        deltas = []
        inc = None
        for i, a in enumerate(angles):
            na = angles[0] if i == len(angles) - 1 else angles[i + 1]
            r = na - a
            if r > math.pi:
                r -= 2 * math.pi
            elif r < -math.pi:
                r += 2 * math.pi
            if r > 0:
                if inc is None:
                    inc = True
                elif not inc:
                    return False
            elif r < 0:
                if inc is None:
                    inc = False
                elif inc:
                    return False
        return True
