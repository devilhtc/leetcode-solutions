# inverse Burrows-Wheeler transform solution of 754 Cracking the Safe [O( k^n * log(k^n) )]
# see Wikipedia: De Bruijn sequence [https://en.wikipedia.org/wiki/De_Bruijn_sequence]

class Solution(object):
    def crackSafe(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        if k == 1:
            return ''.join(['0' for _ in range(n)])
        total = int(pow(k, n))
        sortedEles = sorted([(i % k , i) for i in range(total)])
        collector = []
        visited = [False for _ in range(total)] 
        for i in range(total):
            self.dfs(i, sortedEles, visited, collector)
        outStr = ''.join([str(sortedEles[i][0]) for i in collector])
        outStr = outStr + outStr[:n-1]
        return ''.join(list(reversed(outStr))) # just to conform with tests, reversal is not necessary
    
    def dfs(self, i, sortedEles, visited, collector):
        if visited[i]:
            return 
        collector.append(i)
        visited[i] = True
        ele, j = sortedEles[i]
        self.dfs(j, sortedEles, visited, collector)
        