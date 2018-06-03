class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        n = len(rooms)
        visited = [False for _ in range(n)]
        def bfs(r):
            if visited[r]: return
            visited[r] = True
            for k in rooms[r]: bfs(k)
        bfs(0)
        return all(visited)
        
        