# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def allPossibleFBT(self, N):
        """
        :type N: int
        :rtype: List[TreeNode]
        """
        if N % 2 == 0:
            return []
        dp = [[TreeNode(0)]]

        for i in range(1, N // 2 + 1):
            cur = []
            for j in range(i):
                lc, rc = dp[j], dp[i - 1 - j]
                for l in lc:
                    for r in rc:
                        root = TreeNode(0)
                        root.left = l
                        root.right = r
                        cur.append(root)
            dp.append(cur)

        return dp[N // 2]
