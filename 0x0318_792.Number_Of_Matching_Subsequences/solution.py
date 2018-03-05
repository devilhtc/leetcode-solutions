LOWER_LETTERS = 'abcdefghijklmnopqrstuvwxyz'

class WordCounter(object):
    def __init__(self, words):
        self.words = words
        self.d = {c: [] for c in LOWER_LETTERS}
        self.left = 0
        for w in range(len(words)):
            word = words[w]
            if len(word) > 0:
                self.d[word[0]].append((w, 0))
                self.left += 1
    
    def process(self, c):
        toMove = self.d[c]
        self.d[c] = []
        for w, i in toMove:
            if i == len(self.words[w]) - 1:
                self.left -=1 
            else:
                self.d[self.words[w][i+1]].append((w, i+1))
        return self.left == 0
    
class Solution(object):
    def numMatchingSubseq(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        wc = WordCounter(words)
        for c in S:
            finished = wc.process(c)
            if finished:
                return len(words)
        return len(words) - wc.left