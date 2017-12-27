class Solution(object):
    def countCornerRectangles(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len( grid )
        if m <= 1: return 0
        n = len( grid[0] )
        if n <= 1: return 0
        
        #if m <= n: 
        cache = [[0 for _ in range(m)] for _ in range(m)]
        for j in range(n):
            curOnes = []
            for i in range(m):
                if grid[i][j] == 1:
                    curOnes.append(i)
            for i1 in range(len(curOnes)):
                for i2 in range(i1 + 1, len(curOnes)):
                    cache[curOnes[i1]][curOnes[i2]] += 1
        count = 0
        for i1 in range(m):
            for i2 in range(m):
                count += cache[i1][i2] * (cache[i1][i2] - 1) / 2
        return count
