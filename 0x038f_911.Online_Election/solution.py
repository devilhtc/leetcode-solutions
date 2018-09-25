class TopVotedCandidate:
    def __init__(self, persons, times):
        """
        :type persons: List[int]
        :type times: List[int]
        """
        self.t = -1  # last processed t
        self.i = 0  # num processed so far
        self.persons = persons
        self.times = times
        self.winners = []
        self.p2v = {}
        self.v2p = {}
        self.curmax = 0

    def q(self, t):
        """
        :type t: int
        :rtype: int
        """
        while t > self.t and self.i < len(self.times):
            self.build_next()
        return self._q(t)

    def _q(self, t):
        if t >= self.times[-1]:
            return self.winners[-1]

        lo, hi = 0, self.i
        while hi - lo > 1:
            mi = (lo + hi) // 2
            if self.times[mi] > t:
                hi = mi
            else:
                lo = mi
        return self.winners[lo]

    def build_next(self):
        if self.i >= len(self.times):
            return

        self.t = self.times[self.i]

        p = self.persons[self.i]
        self.p2v[p] = self.p2v.get(p, 0) + 1

        v = self.p2v[p]
        if v not in self.v2p:
            self.v2p[v] = []
        self.v2p[v].append(p)
        if v > self.curmax:
            self.curmax = v

        self.winners.append(self.v2p[self.curmax][-1])
        self.i = self.i + 1


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)
