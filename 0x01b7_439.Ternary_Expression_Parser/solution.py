class Solution:
    def parseTernary(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        stack = []
        d = {}
        for i, c in enumerate(expression):
            if c == "?":
                stack.append(i)
            elif c == ":":
                d[stack.pop()] = i

        def f(s, e):
            if s == e:
                return expression[s]
            if expression[s] == "T":
                return f(s + 2, d[s + 1] - 1)
            else:
                return f(d[s + 1] + 1, e)

        return f(0, len(expression) - 1)
