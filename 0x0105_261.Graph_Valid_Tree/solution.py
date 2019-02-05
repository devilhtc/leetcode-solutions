class Solution:
    def validTree(self, n: "int", edges: "List[List[int]]") -> "bool":
        if n <= 1:
            return True
        visited = set()
        g = collections.defaultdict(list)
        start = None
        all_nodes = set()
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)
            if start is None:
                start = a
            all_nodes.add(a)
            all_nodes.add(b)

        out = [True]

        def dfs(i, p):
            if not out[0]:
                return
            if i in visited:
                out[0] = False
                return
            visited.add(i)
            for c in g[i]:
                if c == p:
                    continue
                else:
                    dfs(c, i)

        visited.add(start)
        for i in g[start]:
            dfs(i, start)

        return out[0] and len(visited) == len(all_nodes) == n
