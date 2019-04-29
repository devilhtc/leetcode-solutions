def c2idx(c):
    return ord(c) - ord("a")


class MyTrie:
    def __init__(self, c):
        self.c = c
        self.isword = False
        self.children = [None] * 26

    def insert(self, w, i=0):
        if i == len(w):
            self.isword = True
            return
        idx = c2idx(w[i])
        if self.children[idx] is None:
            self.children[idx] = MyTrie(w)
        self.children[idx].insert(w, i + 1)

    def query(self, w, i=0):
        if self.isword:
            return True
        if len(w) == i:
            return self.isword
        idx = c2idx(w[i])
        if self.children[idx] is None:
            return False
        return self.children[idx].query(w, i + 1)


class StreamChecker:
    def __init__(self, words: List[str]):
        self.q = collections.deque([])
        self.root = MyTrie("")
        self.ml = 0
        for word in words:
            self.root.insert(list(reversed(word)))
            self.ml = max(self.ml, len(word))

    def query(self, letter: str) -> bool:
        self.q.appendleft(letter)
        if len(self.q) > self.ml:
            self.q.pop()
        return self.root.query(self.q)


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
