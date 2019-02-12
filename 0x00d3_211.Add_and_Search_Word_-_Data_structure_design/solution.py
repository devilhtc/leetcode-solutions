class Trie:
    def __init__(self, c):
        self.c = c
        self.children = [None] * 26


class WordDictionary:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.tries = {}

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        l = len(word)
        if l not in self.tries:
            self.tries[l] = Trie("")
        node = self.tries[l]
        for c in word:
            idx = ord(c) - ord("a")
            if node.children[idx] is None:
                node.children[idx] = Trie(c)
            node = node.children[idx]

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        l = len(word)
        if l not in self.tries:
            return False
        root = self.tries[l]
        found = [False]

        def dfs(node, i):
            if found[0] or i == len(word):
                return True
            c = word[i]
            if c == ".":
                for child in node.children:
                    if found[0]:
                        return True
                    if child and dfs(child, i + 1):
                        found[0] = True
                        return True
            else:
                idx = ord(c) - ord("a")
                child = node.children[idx]
                if child and dfs(child, i + 1):
                    found[0] = True
                    return True
            return False

        return dfs(root, 0)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
