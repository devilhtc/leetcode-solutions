class Solution:
    def deckRevealedIncreasing(self, deck):
        """
        :type deck: List[int]
        :rtype: List[int]
        """
        deck = sorted(deck)
        l = len(deck)

        d = collections.deque(list(range(l)))
        mapping = {}
        for i in range(l):
            j = d.popleft()
            mapping[j] = i
            if len(d) > 0:
                d.append(d.popleft())
        # print(mapping)
        out = [deck[mapping[i]] for i in range(l)]
        return out
