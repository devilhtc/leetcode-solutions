class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        out = []
        stack = []

        def dfs(node):
            stack.append(node)
            if node == len(graph) - 1:
                out.append(list(stack))
            else:
                children = graph[node]
                for c in children:
                    dfs(c)
            stack.pop()

        dfs(0)
        return out
