K = 3


class Trie:
    def __init__(self, nc):
        self.c = nc
        self.children = {}
        self.sentences = []

    def __repr__(self):
        return '<Trie with char "{}">'.format(self.c)


class AutocompleteSystem:
    def __init__(self, sentences, times):
        """
        :type sentences: List[str]
        :type times: List[int]
        """
        self.root = Trie("")
        self.count = {}
        nodes = []

        def insertInTrie(root, sentence):
            cur = root
            for i, c in enumerate(sentence):
                if c not in cur.children:
                    cur.children[c] = Trie(c)
                cur = cur.children[c]
                cur.sentences.append(sentence)

        for s, t in zip(sentences, times):
            self.count[s] = t
            insertInTrie(self.root, s)

        def dfs(n):
            n.sentences = [
                ele[1] for ele in sorted([(-self.count[s], s) for s in n.sentences])[:K]
            ]
            for _, c in n.children.items():
                dfs(c)

        dfs(self.root)
        self.query = []
        self.path = []

    def input(self, c):
        """
        :type c: str
        :rtype: List[str]
        """
        if c == "#":
            out = list(self.path[-1].sentences)
            s = "".join(self.query)
            if s not in self.count:
                self.count[s] = 0

            self.count[s] += 1

            curcount = self.count[s]
            for p in self.path:
                if len(p.sentences) == 0:
                    p.sentences.append(s)
                    continue
                mincount = min([self.count[ps] for ps in p.sentences])
                if len(p.sentences) >= K and curcount < mincount:
                    continue
                curs = []
                for ps in p.sentences:
                    if ps != s:
                        curs.append((-self.count[ps], ps))
                curs.append((-curcount, s))
                curs = sorted(curs)[:K]
                p.sentences = [ele[1] for ele in curs]

            # reset tracking nodes
            self.cur = self.root
            self.query = []
            self.path = []
            return []

        cur = self.root if len(self.path) == 0 else self.path[-1]

        if c not in cur.children:
            cur.children[c] = Trie(c)
        cur = cur.children[c]
        self.path.append(cur)
        self.query.append(c)

        return list(cur.sentences)


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)
