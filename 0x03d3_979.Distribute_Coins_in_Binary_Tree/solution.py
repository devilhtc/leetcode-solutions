# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def distributeCoins(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        _, m = self.helper(root)
        return m

    def helper(self, node):
        if node is None:
            return 0, 0
        ls, lm = self.helper(node.left)
        rs, rm = self.helper(node.right)
        curs = node.val + ls + rs - 1
        curm = lm + rm + abs(ls) + abs(rs)
        # print(curs, curm)
        return curs, curm
