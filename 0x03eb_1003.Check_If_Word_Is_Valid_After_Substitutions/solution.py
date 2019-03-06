class Solution:
    def isValid(self, S: str) -> bool:
        stack = []
        for c in S:
            if c == "a":
                stack.append(1)
            elif len(stack) == 0:
                return False
            elif c == "b":
                if stack[-1] != 1:
                    return False
                stack[-1] = 2
            elif c == "c":
                if stack[-1] != 2:
                    return False
                stack.pop()
        return len(stack) == 0
