# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        rootc = self.prune(root)
        if not rootc:
            return None
        return root
    
    def prune(self, node):
        if node is None: return False
        leftc, rightc = self.prune(node.left), self.prune(node.right)
        if not leftc:
            node.left = None
        if not rightc:
            node.right = None
        return leftc or rightc or node.val == 1
        