class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        def decompose(s):
            out = [[]]
            for i, c in enumerate(s):
                if c.lower() == c or i == 0:
                    out[-1].append(c)
                else:
                    out.append([c])
            return out

        def issubseq(a, b):
            m = 0
            la = len(a)
            for c in b:
                if c == a[m]:
                    m += 1
                if m == la:
                    return True
            return False

        p = decompose(pattern)
        out = []
        for oq in queries:
            q = decompose(oq)
            if len(q) == len(p):
                for i in range(len(p)):
                    if not issubseq(p[i], q[i]):
                        out.append(False)
                        break
                else:
                    out.append(True)
            elif len(q) == len(p) + 1:
                if q[0][0].lower() != q[0][0]:
                    out.append(False)
                    continue
                for i in range(len(p)):
                    if not issubseq(p[i], q[i + 1]):
                        out.append(False)
                        break
                else:
                    out.append(True)
            else:
                out.append(False)
        return out
