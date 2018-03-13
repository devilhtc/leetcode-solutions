class Solution(object):
    def bestRotation(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        d = {}
        n = len(A)
        for i in range(n):
            v = A[i]
            if v > 0 and v < n:
                lose = (i - v + n + 1) % n
                gain = i + 1
                d[lose] = d.get(lose, 0) - 1
                d[gain] = d.get(gain, 0) + 1
        curP = 0
        maxP = 0
        maxI = 0
        for i in range(1, n):
            curP += d.get(i, 0)
            if curP > maxP:
                maxP = curP
                maxI = i
        return maxI

        