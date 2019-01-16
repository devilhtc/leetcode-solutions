class Trie:
    def __init__(self, char):
        self.char = char
        self.children = [None] * 26
        self.words = []


class Solution:
    def addToTrie(self, word):
        node = self.root
        self.root.words.append(word)
        for c in word:
            j = ord(c) - ord("a")
            if node.children[j] is None:
                node.children[j] = Trie(c)
            node = node.children[j]
            node.words.append(word)

    def findInTrie(self, prefix):
        if prefix == "":
            return self.root.words
        node = self.root
        for c in prefix:
            j = ord(c) - ord("a")
            if node.children[j] is None:
                return []
            node = node.children[j]
        return node.words

    def wordSquares(self, words):
        """
        :type words: List[str]
        :rtype: List[List[str]]
        """
        if len(words) == 0:
            return []
        l = len(words[0])
        self.root = Trie("")
        for word in words:
            self.addToTrie(word)

        out = []

        def dfs(stack):
            if len(stack) == l:
                out.append(list(stack))
                return
            n = len(stack)
            prefix = "".join(s[n] for s in stack)
            next_words = self.findInTrie(prefix)
            for word in next_words:
                stack.append(word)
                dfs(stack)
                stack.pop()

        st = []
        dfs(st)

        return out
