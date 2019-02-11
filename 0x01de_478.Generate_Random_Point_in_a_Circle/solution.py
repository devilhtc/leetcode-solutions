class Solution:
    def __init__(self, radius: "float", x_center: "float", y_center: "float"):
        self.r = radius
        self.x = x_center
        self.y = y_center

    def randPoint(self) -> "List[float]":
        if self.r == 0.0:
            return [self.x, self.y]
        a = random.random()
        b = random.random()
        if b > a:
            b = 1 - b
            a = 1 - a
        b = b / a
        x = self.x + a * self.r * math.cos(b * math.pi * 2)
        y = self.y + a * self.r * math.sin(b * math.pi * 2)
        return [x, y]


# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()
