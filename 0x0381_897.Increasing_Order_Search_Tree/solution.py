# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.cur = TreeNode(0)
        head = self.cur
        self.inOrder(root)
        return head.right

    def inOrder(self, node):
        if node is None:
            return
        l, r = node.left, node.right
        self.inOrder(l)
        node.left = None
        self.cur.right = node
        self.cur = node
        self.inOrder(r)
