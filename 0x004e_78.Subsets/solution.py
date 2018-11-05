class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        out = []

        def dfs(cur, i):
            if i < len(nums):
                dfs(cur, i + 1)
                cur.append(nums[i])
                dfs(cur, i + 1)
                cur.pop()
            elif i == len(nums):
                out.append(list(cur))

        dfs([], 0)
        return out
