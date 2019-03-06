class Solution:
    def mergeStones(self, stones: List[int], K: int) -> int:
        if (len(stones) - 1) % (K - 1) != 0:
            # not possible
            return -1

        # cumulative sums to speed up range sum
        cumsums = [0]
        for s in stones:
            cumsums.append(cumsums[-1] + s)

        # memoization,
        # key is (start_index, end_index)
        # value is the min cost of merge it
        # as many times as possible
        memo = {}

        # remaining length
        def rem(s, e):
            return (e - s) % (K - 1) + 1

        def dp(s, e):
            if e - s + 1 < K:
                return 0
            if (s, e) in memo:
                return memo[(s, e)]
            if e - s + 1 == K:
                out = cumsums[e + 1] - cumsums[s]
            else:
                out = float("inf")
                for i in range(s, e):
                    if rem(s, i) + rem(i + 1, e) > K:
                        continue
                    lcost = dp(s, i)
                    rcost = dp(i + 1, e)
                    out = min(out, lcost + rcost)
                if (e - s) % (K - 1) == 0:
                    out = out + cumsums[e + 1] - cumsums[s]
            memo[(s, e)] = out
            return out

        return dp(0, len(stones) - 1)
