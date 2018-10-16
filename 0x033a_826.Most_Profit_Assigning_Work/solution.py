class Solution:
    def maxProfitAssignment(self, difficulty, profit, worker):
        """
        :type difficulty: List[int]
        :type profit: List[int]
        :type worker: List[int]
        :rtype: int
        """
        md = min(difficulty)
        worker = [ele for ele in worker if ele >= md]
        # tuple of difficulty and profit, sorted
        dp = [(difficulty[i], profit[i]) for i in range(len(profit))]
        dp = sorted(dp, key=lambda x: (x[0], -x[1]))
        w = sorted(worker)
        i = j = 0
        mp = dp[0][1]  # max profit
        out = 0
        while j < len(w):
            while i < len(dp) and dp[i][0] <= w[j]:
                mp = max(dp[i][1], mp)
                i += 1
            out += mp
            j += 1
        return out
