class Solution:
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        l = len(S)
        left = [l + 1] * l
        right = [l + 1] * l
        for i, v in enumerate(S):
            if v == C:
                left[i] = 0
            else:
                left[i] = left[i] if i == 0 else left[i - 1] + 1
        for j, v in reversed(list(enumerate(S))):
            if v == C:
                right[j] = 0
            else:
                right[j] = right[j] if (j == l - 1) else right[j + 1] + 1
        return [min(left[i], right[i]) for i in range(l)]
