# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def subtreeWithAllDeepest(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return None

        self.count = 0
        self.cmd = 0
        self.countMD(root, 1)

        self.ans = None
        self.postOrder(root, 1)

        return self.ans

    def postOrder(self, node, d):
        if node is None:
            return 0

        count = 0
        if d == self.cmd:
            count += 1
        count += self.postOrder(node.left, d + 1) + self.postOrder(node.right, d + 1)

        if count == self.count and self.ans is None:
            self.ans = node
        return count

    def countMD(self, node, d):
        if node is None:
            return

        if d == self.cmd:
            self.count += 1
        elif d > self.cmd:
            self.cmd = d
            self.count = 1

        self.countMD(node.left, d + 1)
        self.countMD(node.right, d + 1)
