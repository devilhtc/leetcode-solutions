class Solution:
    def subarrayBitwiseORs(self, A):
        res, cur = set(), set()
        for i in A:
            cur = {i | j for j in cur} | {i}
            res |= cur
        return len(res)
