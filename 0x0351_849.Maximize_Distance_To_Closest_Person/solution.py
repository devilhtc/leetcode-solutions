class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        l = len(seats)
        dl = [0] * (l + 1)
        dr = [0] * (l + 1)
        for i in range(l):
            j = l - i - 1
            dl[i + 1] = 0 if seats[i] == 1 else dl[i] + 1
            dr[j] = 0 if seats[j] == 1 else dr[j + 1] + 1
        return max([max(min(dl[i + 1], dr[i]) for i in range(l)), max(dl[1], dr[0]), max(dl[-1], dr[-2])])