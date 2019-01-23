class Solution:
    def verifyPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: bool
        """
        stack = []
        low = float("-inf")
        for p in preorder:
            if p < low:
                return False
            while len(stack) > 0 and stack[-1] < p:
                low = stack.pop()
            stack.append(p)
        return True
