class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        s = [a, b, c]
        s.sort()
        return [
            1
            if (s[2] - s[1] == 2 or s[1] - s[0] == 2)
            else ((1 if (s[2] - s[1] > 1) else 0) + (1 if (s[1] - s[0] > 1) else 0)),
            s[2] - s[0] - 2,
        ]
