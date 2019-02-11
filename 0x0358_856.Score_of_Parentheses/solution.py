class Solution:
    def scoreOfParentheses(self, S: "str") -> "int":
        stack = []
        for c in S:
            if c == "(":
                stack.append("(")
            else:
                pre = stack[-1]
                if pre == "(":
                    stack.pop()
                    s = 1
                    while len(stack) > 0 and isinstance(stack[-1], int):
                        s += stack.pop()
                    stack.append(s)
                else:
                    s = stack.pop()
                    if stack[-1] == "(":
                        stack.pop()
                    s *= 2
                    while len(stack) > 0 and isinstance(stack[-1], int):
                        s += stack.pop()
                    stack.append(s)
        return stack[-1]
