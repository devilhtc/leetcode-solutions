class Solution(object):
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        area = lambda a, b, c: 0.5 * abs(
            (b[1] - a[1]) * (c[0] - a[0]) - (b[0] - a[0]) * (c[1] - a[1])
        )
        l = len(points)
        maxarea = 0.0
        for i in range(l):
            for j in range(i + 1, l):
                for k in range(j + 1, l):
                    maxarea = max(maxarea, area(points[i], points[j], points[k]))
        return maxarea
