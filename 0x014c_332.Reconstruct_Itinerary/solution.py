# solution: eulerian path from @yangwangx
class Solution:
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        G = collections.defaultdict(list)
        for u, v in tickets:
            G[u].append(v)
        for u in G:
            G[u].sort(reverse=True)

        route = []

        def dfs(at):
            while G[at]:
                to = G[at].pop()
                dfs(to)
            route.append(at)

        dfs("JFK")
        return route[::-1]
