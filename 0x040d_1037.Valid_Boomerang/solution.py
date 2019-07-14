class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        a, b, c = tuple([tuple(ele) for ele in points])
        if a == b or a == c or b == c:
            return False
        dx1, dx2 = a[0] - b[0], a[0] - c[0]
        dy1, dy2 = a[1] - b[1], a[1] - c[1]
        if (dx1 == 0 and dx2 == 0) or (dy1 == 0 and dy2 == 0):
            return False
        return dx1 * dy2 != dy1 * dx2
