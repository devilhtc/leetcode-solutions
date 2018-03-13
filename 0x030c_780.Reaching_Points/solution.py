class Solution(object):
    def reachingPoints(self, sx, sy, tx, ty):
        """
        :type sx: int
        :type sy: int
        :type tx: int
        :type ty: int
        :rtype: bool
        """
        solved = {0 : False}
        def back(i, j):
            #print i, j
            if solved[0]: return
            if i <= 0 or j <= 0 or i == j: return
            if i == sx:
                if j >= sy and (j - sy) % sx == 0: solved[0] = True
                return
            if j == sy:
                if i >= sx and (i - sx) % sy == 0: solved[0] = True    
                return
            if i < j:
                back(i, i if j % i == 0 else j % i)
            else:
                back(j if i % j == 0 else i % j, j)
        back(tx, ty)
        return solved[0]
            
            
            