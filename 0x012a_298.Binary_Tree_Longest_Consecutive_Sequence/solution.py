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
        if root is None:
            return 0
        self.m = 0
        self.helper(root, root.val - 2, 0)
        return self.m
        
    def helper(self, node, pv, pm):
        if node is None:
            return
        if node.val == pv + 1:
            cm = pm + 1
        else:
            cm = 1
        self.m = max(self.m, cm)
        
        for c in [node.left, node.right]:
            self.helper(c, node.val, cm)
            