class Solution(object):
    def kthGrammar(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: int
        """
        if N == 1:
            return 0
        return (self.kthGrammar(N - 1, (K + 1) / 2) + K + 1) % 2
