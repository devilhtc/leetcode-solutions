class Solution:
    def shortestSubarray(self, A: "List[int]", K: "int") -> "int":
        a = collections.deque([])
        cumsum = 0
        a.append((cumsum, 0))
        out = len(A) + 1
        for i, v in enumerate(A):
            cumsum += v
            while len(a) > 0:
                if a[-1][0] >= cumsum:
                    a.pop()
                else:
                    break
            while len(a) > 0:
                presum, j = a[0]
                if cumsum - presum >= K:
                    out = min(out, i + 1 - j)
                    a.popleft()
                else:
                    break
            a.append((cumsum, i + 1))
        return out if out <= len(A) else -1
