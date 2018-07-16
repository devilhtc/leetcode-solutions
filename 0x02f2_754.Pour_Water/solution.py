class Terrain(object):
    def __init__(self, heights):
        self.heights = heights

        # flow in the direction of d, return final index

    def flow(self, k, d):
        # first move the direciton of d to identify the lowest it can achieve
        l = self.heights[k]
        i = k
        while i >= 0 and i < len(self.heights):
            if self.heights[i] <= l:
                l = self.heights[i]
                i += d
            else:
                break
        # then go in the direction of d to identify the first occurrence of l
        i = k
        while i >= 0 and i < len(self.heights):
            if self.heights[i] == l:
                break
            i += d
        return i

        # drop a droplet at position k, the heights will be updated accordingly

    def drop(self, k):
        k = self.flow(k, -1)
        k = self.flow(k, 1)
        self.heights[k] += 1


class Solution(object):
    def pourWater(self, heights, V, K):
        """
        :type heights: List[int]
        :type V: int
        :type K: int
        :rtype: List[int]
        """
        t = Terrain(heights)
        for _ in range(V):
            t.drop(K)
        return t.heights
