# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        self.leaves = {1: [], 2: []}
        self.getLeaves(root1, 1)
        self.getLeaves(root2, 2)
        return self.leaves[1] == self.leaves[2]

    def getLeaves(self, node, key):
        if node is None:
            return
        if node.left is None and node.right is None:
            self.leaves[key].append(node.val)
        self.getLeaves(node.left, key)
        self.getLeaves(node.right, key)
