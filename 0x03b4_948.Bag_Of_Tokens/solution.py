class Solution:
    def bagOfTokensScore(self, tokens, P):
        """
        :type tokens: List[int]
        :type P: int
        :rtype: int
        """
        tokens = sorted(tokens)
        if len(tokens) == 0:
            return 0

        if tokens[0] > P:
            return 0

        a = P
        out = 0
        while out < len(tokens) and a >= tokens[out]:
            a -= tokens[out]
            out += 1

        i = out
        l = len(tokens)
        
        for j in range(l - 1, 0, -1):
            if j <= i:
                break
            a += tokens[j]
            while a >= tokens[i] and i < j:
                a -= tokens[i]
                i += 1
            out = max(i + j - l, out) 
        
        return out