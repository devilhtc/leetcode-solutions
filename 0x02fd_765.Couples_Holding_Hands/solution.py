class Solution(object):
    def minSwapsCouples(self, row):
        """
        :type row: List[int]
        :rtype: int
        """
        n = len(row)/2
        d = [[] for i in range(n)]
        visited = [False for i in range(n)]
        for i in range(n):
            a, b = row[2*i]/2,  row[2*i + 1]/2
            d[a].append(b)
            d[b].append(a)
        def dfs(i):
            if visited[i]: return 0
            visited[i] = True
            return 1 + dfs(d[i][0]) + dfs(d[i][1])
        out = 0
        for i in range(n):
            if not visited[i]:
                out += (dfs(i) - 1)
        return out