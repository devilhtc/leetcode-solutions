class Solution:
    def isEscapePossible(
        self, blocked: List[List[int]], source: List[int], target: List[int]
    ) -> bool:
        # constants
        MAX_STEPS = 204
        BOUNDARY = 1000000
        dij = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        # setup
        blocked_set = set([tuple(point) for point in blocked])
        source_visited = set()
        target_visited = set()
        pq = []
        source = tuple(source)
        target = tuple(target)

        # aliases
        push = heapq.heappush
        pop = heapq.heappop

        # distance metric used for estimation: manhattan distance
        def man_dis(a, b):
            return abs(a[0] - b[0]) + abs(a[1] - b[1])

        # initial state
        push(pq, (man_dis(source, target), source, 0, "S"))
        push(pq, (man_dis(target, source), target, 0, "T"))
        source_visited.add(source)
        target_visited.add(target)
        counts = {"S": 1, "T": 1}
        unbounded = {"S": False, "T": False}

        # use double A* to search for a path from source to target
        while len(pq) > 0:
            _, point, step, start = pop(pq)
            counts[start] -= 1
            if step >= MAX_STEPS:
                unbounded[start] = True
                if unbounded["S" if start == "T" else "T"]:
                    return True
                continue
            if start == "S":
                visited1 = source_visited
                visited2 = target_visited
                reference_point = target
            else:
                visited1 = target_visited
                visited2 = source_visited
                reference_point = source
            if point in visited2:
                return True

            # take the next step
            i, j = point
            for di, dj in dij:
                i2, j2 = i + di, j + dj
                point2 = (i2, j2)
                if (
                    (i2, j2) in blocked_set
                    or (i2, j2) in visited1
                    or not 0 <= i2 < BOUNDARY
                    or not 0 <= j2 < BOUNDARY
                ):
                    continue
                visited1.add((i2, j2))
                push(pq, (man_dis(point2, reference_point), point2, step + 1, start))
                counts[start] += 1

            if (counts["S"] == 0 and not unbounded["S"]) or (
                counts["T"] == 0 and not unbounded["T"]
            ):
                return False
        return False
