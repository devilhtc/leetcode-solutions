class Solution:
    def spellchecker(self, wordlist, queries):
        """
        :type wordlist: List[str]
        :type queries: List[str]
        :rtype: List[str]
        """

        do = {}
        dci = {}
        dv = {}

        def gensigs(w):
            vl = []
            for c in w.lower():
                if c in "aeiou":
                    vl.append("-")
                else:
                    vl.append(c)
            v = "".join(vl)
            return w, w.lower(), v

        for w in wordlist:
            w, ci, v = gensigs(w)
            do[w] = w
            if ci not in dci:
                dci[ci] = w
            if v not in dv:
                dv[v] = w

        out = []
        for q in queries:
            q, ci, v = gensigs(q)
            out.append(do.get(q, dci.get(ci, dv.get(v, ""))))
        return out
