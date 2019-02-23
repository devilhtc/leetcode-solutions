class Solution:
    def shiftingLetters(self, S: str, shifts: List[int]) -> str:
        def shift(c, i):
            n = ord(c) - ord("a")
            return chr((n + i) % 26 + ord("a"))

        l = len(S)
        out = [None] * l
        rs = 0
        for i in range(l):
            j = l - 1 - i
            rs += shifts[j]
            out[j] = shift(S[j], rs)
        return "".join(out)
