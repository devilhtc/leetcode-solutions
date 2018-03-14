import heapq

class Solution(object):
    def swimInWater(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        N = len(grid)
        visited = [[False] * N for _ in range(N)]
        visited[0][0] = True
        boundary = []
        heapq.heappush(boundary, (grid[0][1], 0, 1))
        heapq.heappush(boundary, (grid[1][0], 1, 0))
        visited[1][0], visited[0][1] = True, True
        for t in range(grid[0][0], N * N):
            while len(boundary) > 0 and boundary[0][0] <= t:
                h, i, j = heapq.heappop(boundary)
                if i == N-1 and j == N-1: return t
                for ii, jj in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                    if 0 <= ii < N and 0 <= jj < N:
                        if not visited[ii][jj]:
                            heapq.heappush(boundary, (grid[ii][jj], ii, jj))
                            visited[ii][jj] = True
        return -1
                            
            
            