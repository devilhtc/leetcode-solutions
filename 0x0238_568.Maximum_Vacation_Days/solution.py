class Solution:
    def maxVacationDays(self, flights, days):
        """
        :type flights: List[List[int]]
        :type days: List[List[int]]
        :rtype: int
        """
        n = len(flights)
        if n == 0:
            return 0
        k = len(days[0])
        if k == 0:
            return 0
        dflights = collections.defaultdict(list)
        for i in range(n):
            for j in range(n):
                if flights[i][j]:
                    dflights[i].append(j)
        old = [-1] * n
        old[0] = 0
        for i in range(k):
            new = [old[j] + days[j][i] if old[j] != -1 else -1 for j in range(n)]
            for f, ts in dflights.items():
                if old[f] == -1:
                    continue
                for t in ts:
                    new[t] = max(new[t], old[f] + days[t][i])
            old = new

        return max(old)
