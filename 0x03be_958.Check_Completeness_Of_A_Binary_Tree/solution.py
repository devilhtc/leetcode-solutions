# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def isCompleteTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.helper(root)[1] >= 1

    def helper(self, node):
        if node is None:
            return 0, 2

        ll, lc = self.helper(node.left)
        rl, rc = self.helper(node.right)

        if ll == rl:
            if lc == 2 and rc == 2:
                return ll + 1, 2
            elif lc == 2 and rc == 1:
                return ll + 1, 1
        elif ll == rl + 1:
            if lc >= 1 and rc == 2:
                return ll + 1, 1
        return max(ll, rl) + 1, 0
