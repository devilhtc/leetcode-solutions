class Solution(object):
    def expressiveWords(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        sig = self.gensig(S)
        out = 0
        for w in words:
            if self.isstretchy(self.gensig(w), sig):
                out += 1
        return out

    def gensig(self, s):
        curchar = ""
        count = 0
        out = []
        for i, c in enumerate(s):
            if c == curchar:
                count += 1
            else:
                if count > 0:
                    out.append((curchar, count))
                count = 1
                curchar = c
            if i == len(s) - 1:
                out.append((curchar, count))
        return out

    def isstretchy(self, a, b):
        return len(a) == len(b) and all(
            a[i][0] == b[i][0]
            and (a[i][1] == b[i][1] or (b[i][1] > a[i][1] and b[i][1] >= 3))
            for i in range(len(a))
        )
