class Word(object):
    def __init__(self, word, count):
        self.word = word
        self.count = count

    def __cmp__(self, b):
        if self.count != b.count:
            return self.count - b.count
        else:
            return -1 if self.word > b.word else 1


class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        d = collections.defaultdict(int)
        for w in words:
            d[w] += 1

        pq = []
        for w, c in d.items():
            heapq.heappush(pq, Word(w, c))
            if len(pq) > k:
                heapq.heappop(pq)

        out = []
        while len(pq) > 0:
            out.append(heapq.heappop(pq).word)
        return list(reversed(out))
