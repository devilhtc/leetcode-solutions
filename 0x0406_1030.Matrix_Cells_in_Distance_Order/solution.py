class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        dij = [(0, -1), (-1, 0), (1, 0), (0, 1)]
        q = collections.deque()
        visited = set()
        dist_order = []  # output
        calc_dist = lambda i, j: abs(i - r0) + abs(j - c0)
        is_inbound = lambda i, j: 0 <= i < R and 0 <= j < C
        q.append((r0, c0, 0))
        visited.add((r0, c0))

        while len(q) > 0:
            i, j, d = q.popleft()
            dist_order.append([i, j])
            for di, dj in dij:
                i2, j2 = i + di, j + dj
                d2 = calc_dist(i2, j2)
                if not is_inbound(i2, j2) or (i2, j2) in visited or d2 <= d:
                    continue
                visited.add((i2, j2))
                q.append((i2, j2, d2))

        return dist_order
