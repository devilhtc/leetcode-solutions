# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        self.K = 0
        self.helper(root, root.val, root.val)
        return self.K

    def helper(self, node, a, b):
        if node is None:
            return
        self.K = max([self.K, abs(a - node.val), abs(b - node.val)])
        for child in [node.left, node.right]:
            self.helper(child, min(a, node.val), max(b, node.val))
