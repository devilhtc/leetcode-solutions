class Trie:
    def __init__(self, c):
        self.c = c
        self.children = [None] * 26
        self.word_idx = -1
        # store the indices of strings
        # that have palindrome as the rest of the string
        self.palindrome_rest = []


def is_palindrome(s, i, j):
    """
    s: str
    i, j: start and end indices
    """
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True


class Solution:
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        root = Trie("")

        for i, w in enumerate(words):
            w = w[::-1]
            node = root
            if is_palindrome(w, 0, len(w) - 1):
                node.palindrome_rest.append(i)
            for j, c in enumerate(w):
                idx = ord(c) - ord("a")
                if node.children[idx] == None:
                    node.children[idx] = Trie("c")
                node = node.children[idx]
                if is_palindrome(w, j + 1, len(w) - 1):
                    node.palindrome_rest.append(i)
            node.word_idx = i

        out = []
        for i, w in enumerate(words):
            node = root
            if len(w) == 0:
                for k in node.palindrome_rest:
                    if k != i:
                        out.append([i, k])
                        out.append([k, i])
                continue
            j = 0
            for j, c in enumerate(w):
                idx = ord(c) - ord("a")
                if node.children[idx] == None:
                    break
                node = node.children[idx]
                if j == len(w) - 1:
                    for r in node.palindrome_rest:
                        if r != i:
                            out.append([i, r])
                elif (
                    node.word_idx >= 0
                    and is_palindrome(w, j + 1, len(w) - 1)
                    and node.word_idx != i
                ):
                    out.append([i, node.word_idx])
        return out
