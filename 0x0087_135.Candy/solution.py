class Solution:
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        l = len(ratings)
        if l <= 1:
            return l
        sign = lambda x: 0 if x == 0 else (1 if x > 0 else -1)
        pres = 0
        ups = 0
        downs = 0
        out = 0

        def resolve(u, d):
            o = u * (u + 1) // 2 + d * (d + 1) // 2 + max(u, d) + 1
            return o

        for i in range(1, l + 1):
            curs = sign(ratings[min(i, l - 1)] - ratings[i - 1])
            if curs == 0:
                out += resolve(ups, downs)
                ups = downs = 0
            elif pres < 0 and curs > 0:
                out += resolve(ups, downs)
                ups = downs = 0
                out -= 1
            if curs > 0:
                ups += 1
            elif curs < 0:
                downs += 1
            pres = curs
        return out
