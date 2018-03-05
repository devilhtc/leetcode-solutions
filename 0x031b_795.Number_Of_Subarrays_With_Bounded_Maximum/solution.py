# O(n) time O(1) memory DP solution

class Solution(object):
    def numSubarrayBoundedMax(self, A, L, R):
        """
        :type A: List[int]
        :type L: int
        :type R: int
        :rtype: int
        """
        a = 0 # length of values <= R going back
        b = 0 # distance of values in [L, R] going back
        total = 0
        for i in A:
            if i > R: a, b = 0, 0
            elif i < L: a, b = a + 1, b + (1 if b > 0 else 0)
            else: a, b = a + 1, 1
            total += (a - b + 1 if b > 0 else 0)
        return total
        