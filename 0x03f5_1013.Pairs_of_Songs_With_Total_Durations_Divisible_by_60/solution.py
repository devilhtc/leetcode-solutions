class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        d = {t: 0 for t in range(60)}
        for t in time:
            d[t % 60] += 1
        out = 0
        out += d[0] * (d[0] - 1) // 2
        out += d[30] * (d[30] - 1) // 2
        for k, v in d.items():
            if k == 0 or k >= 30:
                continue
            out += d[k] * d[60 - k]
        return out
