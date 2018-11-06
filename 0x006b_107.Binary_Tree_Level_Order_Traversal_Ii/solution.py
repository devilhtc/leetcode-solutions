# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        self.out = []
        self.inorder(root, 1)
        return list(reversed(self.out))

    def inorder(self, node, level):
        if node is None:
            return
        if level > len(self.out):
            self.out.append([])
        self.inorder(node.left, level + 1)
        self.out[level - 1].append(node.val)
        self.inorder(node.right, level + 1)
