# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.cumsum = 0
        self.helper(root)
        return root

    def helper(self, node):
        if node is None:
            return
        self.helper(node.right)
        self.cumsum += node.val
        node.val = self.cumsum
        self.helper(node.left)
