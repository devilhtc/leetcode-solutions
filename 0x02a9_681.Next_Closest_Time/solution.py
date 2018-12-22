class Solution:
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        day = 24 * 60
        m0 = int(time[:2]) * 60 + int(time[-2:])
        digits = set([int(e) for i, e in enumerate(time) if i != 2])
        nt = ""
        mindiff = -1
        for h1 in digits:
            for h2 in digits:
                h = int(h1 * 10 + h2)
                if h >= 24:
                    continue
                for m1 in digits:
                    for m2 in digits:
                        m = int(m1 * 10 + m2)
                        if m >= 60:
                            continue
                        t = h * 60 + m
                        if t == m0:
                            continue
                        ct = "".join([str(ele) for ele in [h1, h2, ":", m1, m2]])
                        diff = (t - m0 + day) % day
                        if mindiff == -1:
                            nt = ct
                            mindiff = diff
                        else:
                            if diff < mindiff:
                                mindiff = diff
                                nt = ct
        return nt or time
