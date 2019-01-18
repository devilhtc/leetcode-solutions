# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.out = 0
        _, _ = self.lcp(root)
        return self.out

    def lcp(self, node):
        if node is None:
            return 0, 0
        li, ld = self.lcp(node.left)
        ri, rd = self.lcp(node.right)
        ci, cd = 1, 1
        if li and node.left.val + 1 == node.val:
            ci = max(ci, 1 + li)
        if ri and node.right.val + 1 == node.val:
            ci = max(ci, 1 + ri)
        if ld and node.left.val - 1 == node.val:
            cd = max(cd, 1 + ld)
        if rd and node.right.val - 1 == node.val:
            cd = max(cd, 1 + rd)
        self.out = max(self.out, ci + cd - 1)
        return ci, cd
