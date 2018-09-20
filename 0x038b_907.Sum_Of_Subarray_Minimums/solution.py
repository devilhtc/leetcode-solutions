class Solution:
    def sumSubarrayMins(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        stack = []
        extended = [0] + A + [0]
        MOD = 1000000007
        left = [0] * len(extended)
        right = [len(extended) - 1] * len(extended)

        for i, v in enumerate(extended):
            if len(stack) > 0:
                while len(stack) > 0 and stack[-1][0] >= v:
                    w, j = stack.pop()
                    right[j] = i - 1
                if len(stack) == 0:
                    left[i] = i
                else:
                    left[i] = stack[-1][1] + 1
            stack.append((v, i))

        out = 0
        for i, v in enumerate(extended):
            out = (out + (i - left[i] + 1) * (right[i] - i + 1) * v) % MOD
        return out
