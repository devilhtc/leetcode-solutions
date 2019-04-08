class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        s = 0
        out = []
        for c in S:
            if c == "(":
                s += 1
                if s == 1:
                    continue
            else:
                s -= 1
                if s == 0:
                    continue
            out.append(c)
        return "".join(out)
