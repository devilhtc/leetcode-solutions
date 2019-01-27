class Solution:
    def mincostTickets(self, days: "List[int]", costs: "List[int]") -> "int":
        ds = set(days)
        dc = [0] * 366
        for t in range(366):
            if t in ds:
                dc[t] = min(
                    [
                        dc[max(t - 1, 0)] + costs[0],
                        dc[max(t - 7, 0)] + costs[1],
                        dc[max(t - 30, 0)] + costs[2],
                    ]
                )
            elif t > 0:
                dc[t] = dc[t - 1]
        return max(dc)
