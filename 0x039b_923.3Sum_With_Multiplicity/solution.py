import operator as op
from functools import reduce

MOD = 1000000007

def ncr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer//denom

class Solution:
    def threeSumMulti(self, A, target):
        """
        :type A: List[int]
        :type target: int
        :rtype: int
        """
        l = sorted(list(set(A)))
        c = collections.Counter(A)
        out = 0
        for i, v in enumerate(l):
            # 3
            if target == v * 3 and c[v] >= 3:
                out = (out + ncr(c[v], 3)) % MOD 

            # 2 - 1
            r1 = target - v * 2
            if r1 > v and c.get(r1, 0) >= 1 and c.get(v, 0) >= 2:
                out = (out + ncr(c[v], 2) * c[r1]) % MOD

            # 1 - 2
            r2 = target - v
            if r2 // 2 > v and r2 % 2 == 0 and c.get(r2 // 2, 0) >= 2:
                out = (out + ncr(c[r2 // 2], 2) * c[v]) % MOD

            for j in range(i + 1, len(l)):
                v1 = l[j]
                v2 = target - v - v1
                if v2 <= v1:
                    break
                if v2 in c:
                    out = (out + c[v] * c[v1] * c[v2]) % MOD

        return out
