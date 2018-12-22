class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        w2s = collections.defaultdict(list)
        s2w = collections.defaultdict(list)
        if beginWord not in wordList:
            wordList.append(beginWord)
        if endWord not in wordList:
            wordList.append(beginWord)
        for w in wordList:
            wl = list(w)
            for i, c in enumerate(w):
                wl[i] = "_"
                s = "".join(wl)
                w2s[w].append(s)
                s2w[s].append(w)
                wl[i] = c

        wstep = collections.defaultdict(int)
        wstep[beginWord] = 1

        queue = collections.deque([beginWord])
        while len(queue) > 0:
            cw = queue.popleft()
            cstep = wstep[cw]
            for s in w2s[cw]:
                for nw in s2w[s]:
                    if wstep[nw] >= 1 or nw == cw:
                        continue
                    if nw == endWord:
                        return cstep + 1
                    wstep[nw] = cstep + 1
                    queue.append(nw)

        return 0
