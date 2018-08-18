class Solution:
    def spiralMatrixIII(self, R, C, r0, c0):
        """
        :type R: int
        :type C: int
        :type r0: int
        :type c0: int
        :rtype: List[List[int]]
        """
        
        def inbounds(i, j):
            return (
                i >= 0
                and i < R
                and j >= 0 
                and j < C
            )
        
        def getSteps(t):
            return t // 2 + 1
        
        def getDir(t):
            return [
                (0, 1),
                (1, 0),
                (0, -1),
                (-1, 0)
            ][t % 4]
        
        r, c = r0, c0 # current location
        out = [[r, c]] # output
        count = 1 # number of elements counted
        t = 0 # number of turns so far
        
        while count < R * C:
            # get direction and number of steps
            steps = getSteps(t)
            dx, dy = getDir(t)
            
            # move
            for i in range(steps):
                r, c = r + dx, c + dy
                if inbounds(r, c):
                    out.append([r, c])
                    count += 1
                    
            t += 1
            
        return out
        
        