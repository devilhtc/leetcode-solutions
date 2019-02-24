class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        f = {i: 0 for i in range(1, N + 1)}
        t = {i: 0 for i in range(1, N + 1)}
        for i, j in trust:
            f[i] += 1
            t[j] += 1
        for i in range(1, N + 1):
            if f[i] == 0 and t[i] == N - 1:
                return i
        return -1
