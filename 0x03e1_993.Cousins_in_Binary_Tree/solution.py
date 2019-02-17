# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def isCousins(self, root: "TreeNode", x: "int", y: "int") -> "bool":
        self.x = x
        self.y = y
        self.xl = -1
        self.yl = -2
        self.xp = None
        self.yp = None
        self.traverse(root, 0, None)
        return self.xl == self.yl and self.xp != self.yp

    def traverse(self, node, l, p):
        if node is None:
            return
        if node.val == self.x:
            self.xl = l
            self.xp = p
        if node.val == self.y:
            self.yl = l
            self.yp = p
        self.traverse(node.left, l + 1, node.val)
        self.traverse(node.right, l + 1, node.val)
