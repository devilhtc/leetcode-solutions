class Solution:
    def beautifulArray(self, N):
        """
        :type N: int
        :rtype: List[int]
        """
        if N == 1:
            return [1]
        num_odds = (N + 1) // 2
        num_evens = N - num_odds
        l = self.beautifulArray(num_odds)
        r = self.beautifulArray(num_evens)
        return [ele * 2 - 1 for ele in l] + [ele * 2 for ele in r]
