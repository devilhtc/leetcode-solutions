class Solution:
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        pat_rep = self.constructRep(pattern)
        return [word for word in words if self.constructRep(word) == pat_rep]  
    
    def constructRep(self, s):
        out = []
        d = {}
        cur = 0
        for c in s:
            if c not in d:
                d[c] = cur
                cur += 1
            out.append(d[c])
        return out
        