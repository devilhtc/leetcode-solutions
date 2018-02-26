# mathatic one-liner

class Solution(object):
    def escapeGhosts(self, ghosts, target):
        """
        :type ghosts: List[List[int]]
        :type target: List[int]
        :rtype: bool
        """
        return all([ abs(target[0]) + abs(target[1]) < abs(g[0] - target[0]) + abs(g[1] - target[1]) for g in ghosts])
        