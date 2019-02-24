# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def insertIntoMaxTree(self, root: TreeNode, val: int) -> TreeNode:
        def helper(node, val):
            if node is None:
                return TreeNode(val)
            if val > node.val:
                a = TreeNode(val)
                a.left = node
                return a
            node.right = helper(node.right, val)
            return node

        return helper(root, val)
