from collections import deque


class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if len(words) == 0:
            return []
        k = len(words[0])

        g = {}
        for w in words:
            g[w] = g.get(w, 0) + 1
        # print g
        l = len(g)

        # print l
        # each record maintains a queue of words, counts of the words, and the number of counts same as g
        records = [[deque(), {}, 0] for _ in range(k)]
        out = []
        for i in range(len(s) - k + 1):
            record = records[i % k]
            word = s[i : i + k]
            # pop the last word
            prev = ""
            if len(record[0]) == len(words):
                prev = record[0].popleft()
            if prev != "":
                record[1][prev] -= 1
                if record[1][prev] == g[prev]:
                    record[2] += 1
                elif record[1][prev] == g[prev] - 1:
                    record[2] -= 1

            if word in g:
                record[0].append(word)
                record[1][word] = record[1].get(word, 0) + 1
                if record[1][word] == g[word]:
                    record[2] += 1
                elif record[1][word] == g[word] + 1:
                    record[2] -= 1

            else:
                record[0].append("")
            if record[2] == l:
                out.append(i - len(words) * k + k)
            # print i
            # print record
            # print
        return out
