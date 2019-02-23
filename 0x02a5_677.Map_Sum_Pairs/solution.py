class Trie:
    def __init__(self, c, w):
        self.c = c
        self.w = w
        self.children = {}


class MapSum:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = {}
        self.root = Trie("", 0)

    def insert(self, key: "str", val: "int") -> "None":
        if key in self.d:
            newval = val - self.d[key]
            self.d[key] = val
            val = newval
        else:
            self.d[key] = val

        self.root.w += val
        node = self.root
        for c in key:
            if c not in node.children:
                node.children[c] = Trie(c, 0)
            node = node.children[c]
            node.w += val

    def sum(self, prefix: "str") -> "int":
        node = self.root
        for c in prefix:
            if c not in node.children:
                return 0
            node = node.children[c]
        return node.w


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
