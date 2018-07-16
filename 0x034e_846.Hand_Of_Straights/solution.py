class Solution(object):
    def isNStraightHand(self, hand, W):
        """
        :type hand: List[int]
        :type W: int
        :rtype: bool
        """
        if len(hand) % W != 0:
            return False
        d = {}
        cardset = set([])
        for h in hand:
            d[h] = d.get(h, 0) + 1
            cardset.add(h)
        cards = sorted(list(cardset))

        for i in cards:
            while d.get(i, 0) > 0:
                for j in range(i, i + W):
                    if d.get(j, 0) == 0:
                        return False
                    d[j] -= 1

        return True
