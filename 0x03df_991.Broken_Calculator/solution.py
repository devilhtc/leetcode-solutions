class Solution:
    def brokenCalc(self, X: "int", Y: "int") -> "int":
        c = 0
        # deterministic strategy to manipulate Y
        while Y > X:
            if Y % 2 == 1:
                Y = Y + 1
            else:
                Y = Y // 2
            c += 1
        return c + (X - Y)
