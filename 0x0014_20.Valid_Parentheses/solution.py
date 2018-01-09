class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        d = {'(': (0, 1), ')': (0, -1), '{': (1, 1), '}': (1, -1), '[': (2, 1), ']': (2, -1)}
        for p in s:
            i, c = d[p]
            if c == 1:
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                if stack[-1] != i:
                    return False
                stack.pop()
        return len(stack) == 0
        
        
        