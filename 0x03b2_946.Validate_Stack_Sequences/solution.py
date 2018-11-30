class Solution:
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        e2i = {n: i for i, n in enumerate(pushed)}
        stack = []
        i = 0
        for v in popped:
            j = e2i[v]
            while i <= j:
                stack.append(pushed[i])
                i += 1
            if len(stack) == 0 or stack[-1] != v:
                return False
            stack.pop()
        return True
