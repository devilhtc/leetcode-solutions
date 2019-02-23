class Solution:
    def addBoldTag(self, s: str, dict: List[str]) -> str:
        l = len(s)
        ends = [-1] * l
        for x in dict:
            f = 0
            while f != -1 and f < l:
                f = s.find(x, f)
                if f >= 0:
                    ends[f] = max(ends[f], f + len(x) - 1)
                    f += 1
        out = []
        b = False
        end = -1
        for i in range(l):
            if ends[i] >= 0:
                end = max(end, ends[i])
            # flip to bold
            if end >= 0 and not b:
                out.append("<b>")
                b = True
            out.append(s[i])
            # this index must be an end
            # if this is the end and the next one is not bold or the end
            if i == end and (i == l - 1 or ends[i + 1] == -1):
                out.append("</b>")
                end = -1
                b = False
        return "".join(out)
