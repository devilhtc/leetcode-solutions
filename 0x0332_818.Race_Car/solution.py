class Solution:
    def racecar(self, target):
        """
        :type target: int
        :rtype: int
        """
        target = target
        MAXX = target * 2
        # distance to target -> num steps
        memo = {0: -1} 
        queue = [0]
        i = 0
        while i < len(queue):
            cur = queue[i]
            i += 1
            inc = 0
            j = 0
            while True:
                nd = inc - cur
                if abs(nd) > target * 2:
                    break
                if nd not in memo:
                    queue.append(nd)
                    memo[nd] = MAXX
                memo[nd] = min(memo[nd], memo[cur] + j + 1)
                inc += 2 ** j
                j += 1
        return memo[target]