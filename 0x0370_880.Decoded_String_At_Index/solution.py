class Solution(object):
    def decodeAtIndex(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        target = K
        stack = [("", 0)]
        for c in S:
            if not c.isdigit():
                stack.append((c, stack[-1][1] + 1))
            else:
                stack.append((c, stack[-1][1] * int(c)))
            if stack[-1][1] >= K:
                break
        while True:
            if len(stack) == 0:
                break
            if not stack[-1][0].isdigit():
                if stack[-1][1] == target:
                    return stack[-1][0]
                else:
                    stack.pop()
            else:
                target = ((target - 1) % stack[-2][1]) + 1
                stack.pop()
        return ""
