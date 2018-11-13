class Solution:
    def numBusesToDestination(self, routes, S, T):
        """
        :type routes: List[List[int]]
        :type S: int
        :type T: int
        :rtype: int
        """
        if S == T:
            return 0

        stop2buses = collections.defaultdict(list)

        for i, r in enumerate(routes):
            for s in r:
                stop2buses[s].append(i)

        bus_steps = collections.defaultdict(lambda: -1)
        stop_steps = collections.defaultdict(lambda: -1)

        # bfs
        q = [S]
        i = 0
        stop_steps[S] = 0
        while i < len(q):
            s = q[i]
            i += 1

            buses = stop2buses[s]
            step = stop_steps[s]

            for b in buses:
                # if already taken this bus
                if bus_steps[b] >= 0:
                    continue
                bus_steps[b] = step + 1
                stops = routes[b]
                for s2 in stops:
                    if stop_steps[s2] >= 0:
                        continue
                    stop_steps[s2] = step + 1
                    q.append(s2)

        return stop_steps[T]
