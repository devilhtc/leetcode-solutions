class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        def compress(instructions):
            ds = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            x = 0
            y = 0
            d = 0
            for i in instructions:
                if i == "G":
                    x += ds[d][0]
                    y += ds[d][1]
                elif i == "L":
                    d = (d + 3) % 4
                else:
                    d = (d + 1) % 4
            return x, y, d

        x, y, d = compress(instructions)
        if d == 0:
            return x == 0 and y == 0
        if d == 2:
            return x * y == 0 or x == y
        return True
