class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        out = []

        def dfs(num_open, num_left, stack):
            # print(num_open, num_left, stack)
            if num_left < num_open or num_open < 0:
                return
            if num_left == 0:
                if num_open == 0:
                    out.append("".join(stack))
                return
            stack.append("(")
            dfs(num_open + 1, num_left - 1, stack)
            stack.pop()

            stack.append(")")
            dfs(num_open - 1, num_left - 1, stack)
            stack.pop()

        dfs(0, n * 2, [])
        return out
