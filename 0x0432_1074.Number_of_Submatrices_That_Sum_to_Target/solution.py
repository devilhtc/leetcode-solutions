# solution by HungWei-Andy@
class Solution(object):
    def numSubmatrixSumTarget(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: int
        """
        R, C = len(matrix), len(matrix[0])
        stk = [[0] * C]
        res = 0
        for r in range(R):
            nums = [matrix[r][c] + stk[-1][c] for c in range(C)]
            for row in stk:
                cnt = collections.defaultdict(int)
                cnt[0] = 1
                val = 0
                for c in range(C):
                    val += nums[c] - row[c]
                    res += cnt[val - target]
                    cnt[val] += 1
            stk.append(nums)
        return res
