class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        dp = [-1] * (T + 1)
        dp[0] = 0
        for s, e in sorted(clips):
            s = min(s, T)
            e = min(e, T)
            if s == e:
                continue
            if dp[s] != -1:
                for i in range(s + 1, e + 1):
                    dp[i] = dp[s] + 1 if dp[i] == -1 else min(dp[i], dp[s] + 1)
            if dp[T] != -1:
                return dp[T]
        return -1
