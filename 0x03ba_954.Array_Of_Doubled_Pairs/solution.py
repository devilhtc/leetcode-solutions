class Solution(object):
    def canReorderDoubled(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        d = collections.defaultdict(int)
        for ele in A:
            d[ele] += 1
        keys = sorted(list(set(A)), key=lambda x: abs(x))
        for k in keys:
            if k == 0:
                if d[k] % 2 == 1:
                    return False
                continue
            if d[k] == 0:
                continue
            else:
                if d[2 * k] < d[k]:
                    return False
                d[2 * k] -= d[k]
        return True
