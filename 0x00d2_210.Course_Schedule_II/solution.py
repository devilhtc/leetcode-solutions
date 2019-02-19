class Solution:
    def findOrder(
        self, numCourses: "int", prerequisites: "List[List[int]]"
    ) -> "List[int]":
        out = []
        visited = set()
        stack = set()
        g = collections.defaultdict(list)
        valid = [True]

        for i, j in prerequisites:
            g[i].append(j)

        def dfs(i):
            if not valid[0]:
                return
            if i in stack:
                valid[0] = False
                return
            if i in visited:
                return
            visited.add(i)
            stack.add(i)
            for c in g[i]:
                dfs(c)
            stack.remove(i)
            out.append(i)

        for i in range(numCourses):
            dfs(i)

        return out if valid[0] else []
