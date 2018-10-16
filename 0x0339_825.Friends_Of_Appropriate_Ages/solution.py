class Solution:
    def numFriendRequests(self, ages):
        """
        :type ages: List[int]
        :rtype: int
        """
        ages = sorted(ages)
        last_index = {v: i for i, v in enumerate(ages)}
        out = 0
        for i, v in enumerate(ages):
            ub = v  # upper bound is v, inclusive
            lb = v / 2 + 7 + 0.01  # lower bound, exclusive
            if lb > ub:  # empty interval
                continue
            lo, hi = 0, i
            while hi > lo:
                mi = (hi + lo) // 2
                if ages[mi] < lb:
                    lo = mi + 1
                else:
                    hi = mi
            out += last_index[v] - lo
        return out
