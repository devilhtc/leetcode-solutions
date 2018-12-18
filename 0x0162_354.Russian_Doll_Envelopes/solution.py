class Solution:
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        ev = envelopes
        l = len(ev)
        if l == 0:
            return 0

        ev.sort(key=lambda x: (x[0], -x[1]))

        dp = [0] * l
        i = 0
        dp[0] = ev[0][1]
        for k in range(1, l):
            _, h = ev[k]
            if h < dp[0]:
                dp[0] = h
            elif h > dp[i]:
                i += 1
                dp[i] = h
            else:
                lo, hi = 0, i
                while hi > lo:
                    mi = (hi + lo) // 2
                    if h > dp[mi]:
                        lo = mi + 1
                    else:
                        hi = mi
                dp[lo] = h
        return i + 1
