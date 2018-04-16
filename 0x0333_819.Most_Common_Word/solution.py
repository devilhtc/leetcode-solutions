class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        bs = set(banned)
        strip = lambda w: w.strip('!').strip('?').strip('\'').strip(',').strip(';').strip('.')
        words = [strip(word).lower() for word in paragraph.split(' ') if strip(word).lower() not in bs]
        d = {}
        for w in words: d[w] = d.get(w, 0) + 1
        out = w
        for w in d:
            if d[w] > d[out]: out = w
        return out
        