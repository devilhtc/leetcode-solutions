class Solution:
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        c = collections.Counter(deck)
        counts = [v for _, v in c.items()]
        return self.gcdAll(counts) > 1

    def gcdAll(self, counts):
        if len(counts) == 1:
            return counts[0]
        cur = math.gcd(counts[0], counts[1])
        for i in range(2, len(counts)):
            cur = math.gcd(cur, counts[i])
            if cur == 1:
                return cur
        return cur
