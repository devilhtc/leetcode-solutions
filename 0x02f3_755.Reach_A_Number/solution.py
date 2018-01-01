import math

def satisfy(x, n):
    h = (n + 1) * n / 2
    l = -1 * h
    return x >= l and x <= h and (x - l) % 2 == 0
    
class Solution(object):
    def reachNumber(self, target):
        """
        :type target: int
        :rtype: int
        """
        target = abs(target)
        if target <= 1: return target
        b = int(math.sqrt(target * 2 + 1))
        if satisfy(target, b): return b
        if satisfy(target, b + 1): return b + 1
        if satisfy(target, b + 2): return b + 2
        return b + 3